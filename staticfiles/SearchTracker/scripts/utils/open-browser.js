function openInBrowser(url) {
  try {
    const csrfToken = getCsrfTokenFromPage();

    fetch(window.OPEN_BROWSER_URL, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: "url=" + encodeURIComponent(url),
    });
  } catch (err) {
    console.log(err);
  }

  return false;
}
