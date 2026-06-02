const openPdf = $("#open-pdf");

openPdf.on("click", (event) => {
  event.preventDefault();
  openInBrowser(`${window.origin}/${window.PDF_URL}`);
});
