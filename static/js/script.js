function copyURL() {

    const urlField =
        document.getElementById("shortURL");

    if (!urlField) return;

    navigator.clipboard.writeText(
        urlField.value
    ).then(() => {
        alert("URL Copied!");
    }).catch(err => {
        console.error("Failed to copy URL: ", err);
    });
}