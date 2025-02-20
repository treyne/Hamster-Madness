// ==UserScript==
// @name         HamsterKombat URL Finder
// @namespace    http://tampermonkey.net/
// @version      1.7
// @description  Ищет ссылку внутри iframe HamsterKombat, заменяет tgWebAppPlatform=web на tgWebAppPlatform=android и выводит её в консоль (однократно)
// @author       ChatGPT
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function findIframeSrc() {
        let iframe = document.querySelector('iframe[src*="season2.hamsterkombatgame.io"]');
        if (iframe) {
            let modifiedSrc = iframe.src.replace('tgWebAppPlatform=web', 'tgWebAppPlatform=android');
            console.log('Найден iframe, модифицированная ссылка:', modifiedSrc);
            clearInterval(checkInterval);
        }
    }

    let checkInterval = setInterval(findIframeSrc, 1000);
})();
