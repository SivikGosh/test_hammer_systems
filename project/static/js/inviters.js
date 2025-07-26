
import { AppConfig } from "./config.js";


async function showInviters() {
    
    try {
        
        const response = await fetch(`${AppConfig.apiUrl}/api/inviters/`);

        if (!response.ok) {
            throw new Error(`Ошибка ${response.status}`);
        }

        const data = await response.json();

        const ul = document.querySelector('#inviters-list');
        data.inviters.forEach(inviter => {
            const inviterElem = document.createElement('li');
            inviterElem.textContent = inviter;
            ul.appendChild(inviterElem);
        });

    } catch (error) {
        
    }

}


document.addEventListener('DOMContentLoaded', () => {
    showInviters();
});
