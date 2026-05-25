$(() => {
  const contactImgs = $('[id^="contact-img-"]');
  const audio = new Audio();
  let audioPlaying = false;

  contactImgs.on("click", async (event) => {
    event.preventDefault();

    const csrftoken = getCsrfTokenFromPage();

    const contactImgId = event.target.id;
    const contactImgIdSubstrings = contactImgId.split("-");

    const contactId = contactImgIdSubstrings[2];

    let citizenType;
    let citizenSex;
    try {
      const response = await fetch(
        `${window.origin}/api/contacts/id=${contactId}`,
        {
          method: "GET",
        },
      );

      if (!response.ok) throw new Error("Failed to fetch Contact data");

      const data = await response.json();
      citizenType = await data.contact_icon;
      citizenSex = await data.sex;
    } catch (err) {
      console.log("Could not load contact data", err);
    }

    let contactIcons;
    try {
      const response = await fetch(
        `${window.origin}/api/contacts/icons/${citizenSex.toLowerCase()}`,
        {
          method: "GET",
        },
      );

      if (!response.ok) throw new Error("Failed to fetch Contact Icon data");

      contactIcons = await response.json();
      console.log(await contactIcons);
    } catch (err) {
      console.log("Could not load contact icon data", err);
    }

    const contactName = $(`#contact-name-${contactId}`).first().text();

    $("#modal-element").remove();

    const title1 = "Change Contact Icon";
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
                <form id="change-form">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}"></input>
                    <div class="modal-body">
                        <p>${description}</p>
                        <div id="icon-grid" class="icon-grid"></div>
                    </div>
                    <div class="modal-footer d-flex justify-content-between">
                        <button type="button" class="a-button" data-bs-dismiss="modal">Close</button>
                        <button id="change-button" type="button" class="a-button a-button-update" href="">Change</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    `;

    $(".main-content").append(modalHtml);

    const modalElement = $("#modal-element")[0];
    const modal = new bootstrap.Modal(modalElement, { focus: false });

    modal.show();

    $("#modal-element").on("hidden.bs.modal", () => {
      audio.pause();
      audio.currentTime = 0;
      audioPlaying = false;
      $(this).remove();
    });

    // const citizenTypeOptions = JSON.parse(
    //   document.getElementById("citizen-type-options").textContent,
    // );

    // const contactTypeSelect = $("#contact-type").first();

    // if (contactTypeSelect.children().length < citizenTypeOptions.length) {
    //   for (let i = 0; i < citizenTypeOptions.length; ++i) {
    //     const optionValue = citizenTypeOptions[i];
    //     const selected = optionValue === citizenType;

    //     const newOption = `
    //     <option id="opt-${i}" value="${optionValue}">
    //         ${optionValue}
    //     </option>
    //     `;
    //     contactTypeSelect.append(newOption);
    //   }
    // }

    // contactTypeSelect.val(citizenType);

    // contactTypeSelect.on("change", (event) => {
    //   const selectedText = $(event.target).val();

    //   const audioFileArray = selectedText.toLowerCase().split(" ");

    //   let audioFile = "";
    //   for (substring of audioFileArray) {
    //     audioFile += substring + "-";
    //   }

    //   audioFile = audioFile.substring(0, audioFile.length - 1);
    //   audioFile += ".mp3";

    //   if (audioPlaying) {
    //     audio.pause();
    //     audio.currentTime = 0;
    //   } else {
    //     try {
    //       audio.src = `${window.location.origin}/static/SearchTracker/audio/${audioFile}`;
    //       audio.play();
    //       audioPlaying = true;
    //       audio.onended = () => {
    //         audioPlaying = false;
    //       };
    //     } catch (err) {
    //       console.log(err);
    //     }
    //   }
    // });

    const gridContainer = $("#icon-grid");
    let selectedIconId = citizenType.id;

    contactIcons.forEach((icon) => {
      const isSelected = icon.id == selectedIconId;
      const imageUrl = `${window.origin}/static/SearchTracker/images/icons/${icon.icon_file}.png`;

      const cleanedIconName = icon.icon_name.replace(citizenSex, "").trim();

      const cardHtml = `
      <div class="icon-card ${isSelected ? "selected" : ""}" data-icon-id="${icon.id}" data-icon-name="${icon.icon_name}">
        <input 
          type="radio" 
          id=${icon.id} 
          class="icon-radio ${isSelected ? "selected" : ""}" 
          name="contact-icon" 
          value=${icon.id} 
        />
        <img src=${imageUrl} alt="${icon.icon_name} icon" loading="lazy" />
        <p class="icon-name">${cleanedIconName}</p>
      </div>
      `;

      const card = $(cardHtml);

      card.on("click", (event) => {
        event.stopPropagation();
        const radio = card.find('input[type="radio"]');
        radio.prop("checked", true);
        selectedIconId = icon.id;

        gridContainer.find(".icon-card").removeClass("selected");
        card.addClass("selected");

        const selectedName = icon.icon_name;

        if (!selectedName.toLowerCase().includes("drone")) {
          let audioFile = "";
          let audioSrc = `${window.location.origin}/static/SearchTracker/audio/contacts/`;

          if (selectedName == "Technician") {
            const breenId = Math.floor(Math.random() * 34) + 1;
            audioFile = `breen${breenId}`;
            audioSrc = `${audioSrc}breen/${audioFile}`;
          } else {
            const audioFileArray = selectedName.toLowerCase().split(" ");
            for (substring of audioFileArray) {
              audioFile += substring + "-";
            }
            audioFile = audioFile.substring(0, audioFile.length - 1);
            audioSrc = `${audioSrc}${citizenSex.toLowerCase()}/${audioFile}`;
          }

          audioSrc += ".mp3";

          audio.pause();
          audio.currentTime = 0;
          audioPlaying = false;

          try {
            audio.src = audioSrc;
            audio.play();
            audioPlaying = true;
            audio.onended = () => {
              audioPlaying = false;
            };
          } catch (err) {
            console.log(err);
          }
        } else {
          audio.pause();
          audio.currentTime = 0;
          audioPlaying = false;
        }
      });

      gridContainer.append(card);
    });

    const changeForm = $("#change-form");
    const changeButton = $("#change-button");

    changeButton.on("click", (event) => {
      event.preventDefault();

      const formData = new URLSearchParams();
      formData.append("icon-id", selectedIconId);

      fetch(`${window.location}id=${contactId}/icon/change/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": csrftoken,
        },
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            console.log(data.redirect_url);
            window.location.href = data.redirect_url;
          }
        })
        .catch((err) => {
          console.log("Update error: ", err);
          alert(
            `An error occured when attempting to update the contact id for contact, ${contactName}`,
          );
        });
    });
  });
});
