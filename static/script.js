document.addEventListener("DOMContentLoaded", () => {
    // dom이 다 로딩된뒤(html이 그려진 뒤) 실행
    fetch("/api/data")
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("result").textContent = data.message;
        })
        .catch((error) => {
            document.getElementById("result").textContent = "데이터 불러오기 실패";
            console.error(error);
        });
});