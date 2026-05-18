function getCsrfTokenFromPage() {
  const tokenInput = document.querySelector(
    'input[name="csrfmiddlewaretoken"]',
  );
  return tokenInput ? tokenInput.value : null;
}
