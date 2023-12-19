import {STATUS_CODES} from "../consts.js";

export function fastFightSubmitHandler(e) {
    e.preventDefault();
    const form = $("#fast-fight-form");
    $.ajax({
        type: "GET",
        url: form.attr("action"),
        data: form.serialize(),
        dataType: "json",
        success: function (data) {
            let battle_log = $("#battle-log");
            $("#opponent_hp").attr("value", data.opponent_pokemon.hp);
            $("#player_hp").attr("value", data.player_pokemon.hp);
            data.description_list.forEach((element) =>
                battle_log.append($("<div>").append(document.createTextNode(element.description + "\n")))
            )
            if (data.player_pokemon.hp === 0) {
                $("#revenge-form").css("display", "block");
            }
            $("#fast-fight-submit").attr("disabled", "disabled");
            $("#hit-submit").attr("disabled", "disabled");
            $("#battle-form").css("display", "block");
            $("#email-form").css("display", "block");
        },
        statusCode: STATUS_CODES,
    });
}

export function addFastFightEventListeners() {
    document.getElementById("fast-fight-form").addEventListener("submit", fastFightSubmitHandler);
}
