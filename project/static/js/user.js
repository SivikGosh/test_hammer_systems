import { AppConfig } from "./config.js";


async function showUserInfo() {

    const user = window.currentUser;

    try {

        const response = await fetch(`${AppConfig.apiUrl}/api/users/${user}`);

        if (!response.ok) {
            throw new Error(`Ошибка ${response.status}`);
        }

        const data = await response.json();

        const ul = document.querySelector('#user-info-form ul');

        const userPhone = document.createElement('li');
        userPhone.textContent = `Телефон: ${data.phone_number}`;
        ul.appendChild(userPhone);

        const userFirstName = document.createElement('li');
        userFirstName.textContent = `Имя: ${data.first_name}`;
        const firstNameeditBtn = document.createElement('button');
        firstNameeditBtn.textContent = `Редактировать`;
        firstNameeditBtn.disabled = true;
        firstNameeditBtn.style.float = 'right';
        userFirstName.appendChild(firstNameeditBtn);
        ul.appendChild(userFirstName);

        const userLastName = document.createElement('li');
        userLastName.textContent = `Фамилия: ${data.last_name}`;
        const lastNameeditBtn = document.createElement('button');
        lastNameeditBtn.textContent = `Редактировать`;
        lastNameeditBtn.disabled = true;
        lastNameeditBtn.style.float = 'right';
        userLastName.appendChild(lastNameeditBtn);
        ul.appendChild(userLastName);

    } catch (error) {
        console.error('Ошибка запроса:', error);
    }
}


document.addEventListener('DOMContentLoaded', () => {
    showUserInfo();
});
