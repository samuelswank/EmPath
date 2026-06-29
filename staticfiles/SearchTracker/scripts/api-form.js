$(() => {
  const apiUrlBtns = $(".api-button");

  const btnsRequiringForm = apiUrlBtns.filter((index, element) => {
    return $(element).text().indexOf("<") !== -1;
  });

  btnsRequiringForm.each((index, element) => {
    const pattern = $(element).text().trim();
    const parsedPattern = parseUrlPattern(pattern);

    const btnId = $(element).attr("id");
    const apiPathName = btnId.slice(0, btnId.length - 4);

    const apiFormCollapse = $(`#${apiPathName}-collapse`);

    parsedPattern.vars.forEach((variable) => {
      const varContainer = $('<div class="input-group"></div>');
      const varLabel = $(`<label for=$>${variable["var"]}</label>`);

      let varInput;
      let inputType = "text";
      if (variable.datatype === "int") {
        inputType = "number";
        varInput = $(
          `<input 
            id="${apiPathName}-${variable["var"]}" 
            name=${variable["var"]} 
            type="${inputType}" 
            min="0"
          />`,
        );
      }

      if (varInput) {
        varContainer.append(varLabel);
        varContainer.append(varInput);
      }

      apiFormCollapse.append(varContainer);
    });

    $(element).on("click", async (event) => {
      event.preventDefault();

      const inputs = [];
      const inputElements = $(`input[id^="${apiPathName}-"]`);

      inputElements.each((index, element) => {
        const value = $(element).val();
        inputs.push(value);
      });

      let patternIdx = 0;
      let varIdx = 0;
      let urlStr = "";

      while (patternIdx < parsedPattern.template.length) {
        urlStr += parsedPattern.template[patternIdx];
        if (varIdx < inputs.length) {
          urlStr += inputs[varIdx];
          ++varIdx;
        }
        ++patternIdx;
      }

      urlStr = `${window.origin}/api/${urlStr}`;

      try {
        openNewWindow(urlStr);
      } catch (err) {
        alert(err);
      }
    });
  });

  function parseUrlPattern(pattern) {
    const regex = /<([^:]+):([^>]+)>/g;
    const vars = [];
    let template = pattern;
    let match;

    let templateArray;

    while ((match = regex.exec(pattern)) !== null) {
      const datatype = match[1];
      const varName = match[2];

      vars.push({ datatype, var: varName });
      template = template.replace(match[0], `|`);

      templateArray = template.split("|");
      templateArray = templateArray.filter((substring) => substring.length > 0);
    }

    return { template: templateArray, vars };
  }
});
