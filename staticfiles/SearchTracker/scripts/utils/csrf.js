function getCsrfTokenFromPage() {
  const tokenInput = $('input[name="csrfmiddlewaretoken"]');
  return tokenInput.length > 0 ? tokenInput[0].value : null;
}
