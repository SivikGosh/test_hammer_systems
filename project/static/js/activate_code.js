import { AppConfig } from "./config.js";
import { prePostValidation, postData } from "./utils.js";


async function activateCode() {

    const payload = { activate_code: document.getElementById('activateCodeInput').value };

    prePostValidation(payload.activate_code, AppConfig.activateCodeRegex)

    try {
        
        const response = await fetch(
            `${AppConfig.apiUrl}/api/activate_code/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': AppConfig.csrftoken
                },
                body: JSON.stringify(payload)
            }
        );

        const data = await response.json();

        if (response.status === 200) {alert(data.message); location.href = location.href;};
        if (response.status === 403) {alert(data.message);};
        if (response.status === 404) {alert(data.message);};


    } catch (error) {
        console.error('Ошибка запроса:', error);
    }

}


document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector("#user-info-form ul button");
    btn?.addEventListener("click", activateCode);
});
