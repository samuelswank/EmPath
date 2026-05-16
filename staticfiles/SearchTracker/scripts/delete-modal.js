$(() => {
  const deleteAnchors = $('[id^="delete-"]');

  deleteAnchors.on("click", (event) => {
    event.preventDefault();

    const csrftoken = getCsrfTokenFromPage();

    const anchorId = event.target.id;
    const anchorIdSubstrings = anchorId.split("-");

    let recordType = anchorIdSubstrings[1];

    const recordId = anchorIdSubstrings[anchorIdSubstrings.length - 1];
    const recordName = $(`[id="${recordType}-name-${recordId}"]`).text();

    recordType = capitalizeFirstLetter(recordType);

    const title = "Perhaps a careful review of your options is in order.";
    const body = `Are you sure that you wish to delete <strong>${recordType}</strong> with id = <i>${recordId}</i>, <strong>${recordName}</strong>.`;

    const modalHtml = `
    <div id="modal-element" class="modal fade" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">${title}</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p>${body}</p>
                </div>
                <div class="modal-footer d-flex justify-content-between">
                    <button type="button" class="a-button" data-bs-dismiss="modal">Close</button>
                    <form action="/template-snippets/delete/id=${recordId}" method="post">
                        <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}"></input>
                        <button id="delete" type="submit" class="a-button a-button-delete" href="">Delete</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    `;

    $(".main-content").append(modalHtml);

    const modalElement = $("#modal-element")[0];
    const modal = new bootstrap.Modal(modalElement);

    modal.show();

    const audio = new Audio(window.DELETE_AUDIO_PATH);
    audio.play();
  });
});

function capitalizeFirstLetter(string) {
  return String(string).charAt(0).toUpperCase() + String(string).slice(1);
}
