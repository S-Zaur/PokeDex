import {toast} from "./toast.js";

export const mainContainer = document.getElementById("main-container");
export const STATUS_CODES = {
    400: function () {
        toast("Ошибочный запрос");
    }, 403: function () {
        toast("Запрещено");
    }, 404: function () {
        toast("Не найдено");
    }, 500: function () {
        toast("Ошибка");
    }
}
