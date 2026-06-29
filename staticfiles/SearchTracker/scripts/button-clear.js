const buttonClear = $("#button-clear");

buttonClear.on("click", () => {
  const filtersetForm = $("#filterset-form");

  console.log(filtersetForm);

  const inputsEntryArray = ["text", "email", "password", "number"];
  let inputsEntryString = "";
  inputsEntryArray.forEach((inputType) => {
    inputsEntryString += `input[type="${inputType}"], `;
  });

  inputsEntryString = inputsEntryString.substring(
    0,
    inputsEntryString.length - 2,
  );
  const inputsEntry = filtersetForm.find(inputsEntryString);

  inputsEntry.toArray().forEach((inputEntry) => {
    inputEntry.value = "";
  });

  const checkboxes = filtersetForm.find('input[type="checkbox"]');
  checkboxes.toArray().forEach((checkbox) => {
    checkbox.checked = false;
  });

  const selectElements = filtersetForm.find("select");
  selectElements.toArray().forEach((selectElement) => {
    selectElement.selectedIndex = 0;
  });
});
