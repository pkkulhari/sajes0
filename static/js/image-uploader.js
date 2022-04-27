$(function () {
  // Open file selecor when clicked on drop region
  const fakeInput = document.createElement("input");
  fakeInput.type = "file";
  fakeInput.accept = "image/jpeg,image/png";
  fakeInput.multiple = true;

  $(".iu")
    .on("click", () => fakeInput.click())
    .on("click", ".iu__preview--image", (e) => e.stopPropagation());

  // Prevent default behavior of browser and stop propagation
  const preventDefault = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  $(".iu")
    .on("dragenter", preventDefault)
    .on("dragout", preventDefault)
    .on("dragover", preventDefault)
    .on("drop", preventDefault);

  // Handle files
  fakeInput.addEventListener("change", (e) => handleFiles(e.target.files));
  $(".iu").on("drop", (e) => handleFiles(e.originalEvent.dataTransfer.files));

  function handleFiles(files) {
    for (const file of files) {
      if (validateImage(file)) {
        // compression
        new Compressor(file, {
          quality: 0.6,
          success: (compressedImage) => {
            compressedImage["uuid"] = uuidv4();
            imagePreview(compressedImage);
            imageUpload(compressedImage);
          },
        });
      }
    }
  }

  // Validate images
  function validateImage(image) {
    const validTypes = ["image/jpeg", "image/png"];
    const maxSize = 5e6; // 5 MB

    if (!validTypes.includes(image.type)) {
      alert("Invalid image type, only '.png' or '.jpeg' are allowed.");
      return false;
    }

    if (image.size > maxSize) {
      alert("Image too large, max image size is 5 MB");
      return false;
    }

    return true;
  }

  // Image preview
  function imagePreview(image) {
    const reader = new FileReader();
    reader.onload = (e) => {
      const src = e.target.result;

      $(`<div class="iu__preview--image" id="${image.uuid}">
          <img src="${src}">
          <div class="overlay" style="width: 100%;"></div>
        </div>`)
        .appendTo(".iu__preview")
        .append('<span class="remove">Remove</span>')
        .on("click", (e) => {
          imageDelete(e.target.parentElement.id);
          e.stopPropagation();
        });
    };

    reader.readAsDataURL(image);
  }

  // Upload image
  function imageUpload(image) {
    const url = $("#imageUploader").attr("data-action-create");
    const csrfToken = $("#imageUploader").attr("data-csrf-token");

    const formData = new FormData();
    formData.append("image", image);
    formData.append("imageUUID", image.uuid);

    $.post({
      url: url,
      headers: { "X-CSRFToken": csrfToken },
      data: formData,
      contentType: false,
      processData: false,

      xhr: () => {
        const xhr = new XMLHttpRequest();
        xhr.upload.addEventListener("progress", (e) => {
          const perc = (e.loaded / e.total) * 100 || 100;
          const width = `${100 - perc}%`;

          $(`#${image.uuid}`).children(".overlay").css("width", width);
        });

        return xhr;
      },
    });
  }

  // Delete Image
  window.imageDelete = (uuid) => {
    const url = $("#imageUploader").attr("data-action-delete");
    const csrfToken = $("#imageUploader").attr("data-csrf-token");

    $.post({
      url: url,
      headers: { "X-CSRFToken": csrfToken },
      data: { imageUUID: uuid },
    });

    $(`#${uuid}`).remove();
  };
});
