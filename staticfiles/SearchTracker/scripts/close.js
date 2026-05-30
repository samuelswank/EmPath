const closeAudio = new Audio(
  `${window.origin}/static/SearchTracker/audio/close.mp3`,
);
let closeAudioPlaying = false;

const closeButton = $("#close");

closeButton.on("click", (event) => {
  event.preventDefault();

  closeAudio.play();

  const iconSrcPath = `${window.origin}/static/SearchTracker/images/icons/`;

  const title = "Please Don't Go!";
  const body = `
    <div class="d-flex align-items-center text-center">
        <p class="mb-0 me-2">The drones need you.</p>
        <img class="icon-close me-1" src="${iconSrcPath}drone-male.png" alt="Male Drone icon" />
        <img class="icon-close" src=${iconSrcPath}drone-female.png alt="Female Drone icon" />
    </div>
    <p>They look up to you. &#129402;</p>
  `;

  const modalHtml = `
    <div id="modal-close" class="modal fade" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title text-center">${title}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    ${body}
                </div>
                <div class="modal-footer d-flex justify-content-between">
                    <button type="button" class="a-button" data-bs-dismiss="modal">Return</button>
                    <button id="confirm-close" type="submit" class="a-button a-button-delete">Close</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    `;

  $(".main-content").append(modalHtml);

  const modalClose = $("#modal-close")[0];
  const closeModal = new bootstrap.Modal(modalClose);

  closeModal.show();

  $("#modal-close").on("hidden.bs.modal", () => {
    closeAudio.pause();
    closeAudio.currentTime = 0;
    audioPlaying = false;
    $(this).remove();
  });

  const confirmCloseButton = $("#confirm-close");

  confirmCloseButton.on("click", (event) => {
    event.preventDefault();

    fetch(`${window.origin}/close`).then((err) => {
      console.log("Error closing program", err);
      alert(`Error closing program:
${err}`);
    });
  });
});
