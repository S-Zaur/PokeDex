import {STATUS_CODES} from "../consts.js";
import {toast} from "../toast.js";

export function ftpSaveSubmitHandler(e) {
    e.preventDefault();
    const form = $("#ftp-save-form");
    $.ajax({
        type: "POST",
        url: form.attr("action"),
        data: form.serialize(),
        dataType: "json",
        success: function (data) {
            toast("ok");
        },
        statusCode: STATUS_CODES,
    });
}

export function addFtpSaveEventListeners() {
    document.getElementById("ftp-save-form").addEventListener("submit", ftpSaveSubmitHandler);
}

