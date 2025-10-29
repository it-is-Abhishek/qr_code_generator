async function generateQR() {
const text = document.getElementById("text").value;
    const response = await fetch("/generate", {
        method : "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text: text })
    });
    if (response.ok){
        const blob = await response.blob();
        document.getElementById("qrImage").src = URL.createObjectURL(blob);
    }
    else{
        alert("Error generating QR!")
    }
}
