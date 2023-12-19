import {STATUS_CODES} from "../consts.js";

export function emailSubmitHandler(e) {
    e.preventDefault();
    const form = $("#email-form")
    $.ajax({
        type: "POST",
        url: form.attr("action"),
        data: form.serialize(),
        dataType: "json",
        statusCode: STATUS_CODES,
    });
}

export function addEmailEventListeners() {
    document.getElementById("email-form").addEventListener("submit", emailSubmitHandler);
}

