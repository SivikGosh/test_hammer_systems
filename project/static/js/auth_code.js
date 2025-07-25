import { AppConfig } from "./config.js";
import { postData, prePostValidation, resendCodeCount, sleep } from "./utils.js";


async function getAuthCode() {

    const payload = { phone_number: document.getElementById('phoneInput').value };

    prePostValidation(payload.phone_number, AppConfig.phoneRegex)

    try {

        document.getElementById("wait-code-message").style.display = "block";
        await sleep(2000);
        document.getElementById("wait-code-message").style.display = "none";

        const data = await postData(`${AppConfig.apiUrl}/api/auth_code/`, payload);

        localStorage.setItem('phoneNumber', payload.phone_number);

        document.getElementById("phone-number-form").style.display = "none";
        document.getElementById("auth-code-form").style.display = "block";
        document.getElementById("countdown-block").style.display = "block";

        alert(`Код доступа ${data.code}. Будет актуален в течение ${AppConfig.codeTTL} секунд.`);

        resendCodeCount(AppConfig.codeTTL)

    } catch (error) {
        console.error('Ошибка запроса:', error);
    }
}


document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("get-code-btn");
    btn?.addEventListener("click", getAuthCode);
});
