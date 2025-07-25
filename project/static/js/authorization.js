import { AppConfig } from "./config.js";
import { postData, prePostValidation } from "./utils.js";


async function authorization() {

    const payload = { auth_code: document.getElementById('codeInput').value };
    payload.phone_number = localStorage.getItem('phoneNumber');

    prePostValidation(payload.auth_code, AppConfig.codeRegex)

    try {
        const data = await postData(`${AppConfig.apiUrl}/api/authorization/`, payload);
        window.location.href = AppConfig.apiUrl + data.redirect_url;
    } catch (error) {
        console.error('Ошибка запроса:', error);
    }

}


document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("authorize-btn");
  btn?.addEventListener("click", authorization);
});
