function copyURL() {

    const urlField =
        document.getElementById("shortUrl");

    navigator.clipboard.writeText(
        urlField.value
    );

    alert("URL Copied!");
}