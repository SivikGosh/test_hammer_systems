import { AppConfig } from "./config.js";


export async function postData(url, payload) {

    const response = await fetch(
        url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': AppConfig.csrftoken
            },
            body: JSON.stringify(payload)
        }
    );

    if (!response.ok) {
        if (response.status == 403) {
            alert('Введён неправильный или неактуальный код.');
        } else { throw new Error(`Ошибка ${response.status}`); }
    }

    const data = await response.json();

    return data;
}


export function prePostValidation(data, regex) {
    if (!data) {alert('Вы не ввели данные.'); return;}
    if (!regex.test(data)) {alert('Неверный формат данных.'); return;}
}


export function resendCodeCount(seconds) {

    const countdownElement = document.getElementById('countdown');
    countdownElement.style.display = "inline";

    const countdownBlock = document.getElementById('countdown-block');
    const codeDeprecated = document.getElementById('auth-code-deprecated');
    codeDeprecated.style.display = "none";

    const interval = setInterval(() => {
        seconds--;
        countdownElement.textContent = seconds;
        if (seconds <= 0) {
            clearInterval(interval);
            countdownBlock.style.display = "none";
            document.getElementById("auth-code-form").style.display = "none";
            document.getElementById("phone-number-form").style.display = "block";
            codeDeprecated.style.display = "block";
        }
    }, 1000);
}


export function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
