$(() => {
  const contactImgs = $('[id^="contact-img-"]');
  const audio = new Audio();
  let audioPlaying = false;

  contactImgs.on("click", (event) => {
    event.preventDefault();

    const csrftoken = getCsrfTokenFromPage();

    const contactImgId = event.target.id;
    const contactImgIdSubstrings = contactImgId.split("-");

    const contactId = contactImgIdSubstrings[2];
    const contactName = $(`#contact-name-${contactId}`).first().text();

    const title1 = "Change Contact Type";
    const description =
      "Will you demote, promote, transcend, or nerve staple them?";

    const modalHtml = `
    <div id="modal-element" class="modal fade" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">${title1}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form>
                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}"></input>
                    <div class="modal-body">
                        <p>${description}</p>
                        <div class="select-container">
                            <label for="contact-type" class="form-label">
                                Icon
                            </label>
                            <select id="contact-type" class="modal-select">
                            </select>
                        </div>
                    </div>
                    <div class="modal-footer d-flex justify-content-between">
                        <button type="button" class="a-button" data-bs-dismiss="modal">Close</button>
                        <button id="change" type="submit" class="a-button a-button-update" href="">Change</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    `;

    $(".main-content").append(modalHtml);

    const modalElement = $("#modal-element")[0];
    const modal = new bootstrap.Modal(modalElement);

    modal.show();

    const citizenTypeOptions = JSON.parse(
      document.getElementById("citizen-type-options").textContent,
    );

    const contactTypeSelect = $("#contact-type").first();

    for (let i = 0; i < citizenTypeOptions.length; ++i) {
      const newOption = `
        <option id=${i}>
            ${citizenTypeOptions[i]}
        </option>
        `;
      contactTypeSelect.append(newOption);
    }

    contactTypeSelect.on("change", (event) => {
      const selectedText = $(event.target)
        .find("option:selected")
        .text()
        .trim();

      const audioFileArray = selectedText.toLowerCase().split(" ");

      let audioFile = "";
      for (substring of audioFileArray) {
        audioFile += substring + "-";
      }

      audioFile = audioFile.substring(0, audioFile.length - 1);
      audioFile += ".mp3";

      if (audioPlaying) {
        audio.pause();
        audio.currentTime = 0;
      } else {
        try {
          audio.src = `${window.location.origin}/static/SearchTracker/audio/${audioFile}`;
          audio.play();
          audioPlaying = true;
          audio.onended = () => {
            audioPlaying = false;
          };
        } catch (err) {
          console.log(err);
        }
      }
    });
  });
});
