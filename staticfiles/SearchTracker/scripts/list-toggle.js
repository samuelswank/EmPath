$(document).ready(() => {
  const $toggle = $("#table-toggle");
  const $documentContainer = $("#table-container-documents");
  const $snippetContainer = $("#table-container-snippets");
  const $options = $(".segmented-option");
  const hiddenClass = "table-container-hidden";

  function updateToggle(checked) {
    if (checked) {
      $options.first().removeClass("active");
      $options.last().addClass("active");
      $documentContainer.addClass(hiddenClass);
      $snippetContainer.removeClass(hiddenClass);
    } else {
      $options.first().addClass("active");
      $options.last().removeClass("active");
      $documentContainer.removeClass(hiddenClass);
      $snippetContainer.addClass(hiddenClass);
    }
  }

  $options.on("click", function () {
    const isChecked = $toggle.prop("checked");
    const newValue = $(this).data("value");
    const shouldBeChecked = newValue === "snippets";

    if (shouldBeChecked !== isChecked)
      $toggle.prop("checked", shouldBeChecked).trigger("change");
  });

  $toggle.on("change", function () {
    updateToggle($(this).is(":checked"));
  });

  updateToggle($toggle.is(":checked"));
});
