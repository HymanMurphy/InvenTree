{% load static %}

<script type="text/javascript" src="{% static 'script/delay.js' %}">
</script>

<script type="text/javascript">

function add_part(part) {
    var text = "<tr>";

    text += "<td><a href='" + part.url + "'>" + part.name + "</a></td>";
    text += "<td>" + part.description + "</td>";

    text += "<td>";

    // TODO - Work out how to add in category name + link...
    if (part.category){
        text += '<a href="/part/category/' + part.category + '/">';
        text += part.category_path;
        text += '</a>';
    }

    text += "</td>";

    text += "</tr>";

    $("#part-list").append(text);
}

function filter_parts(text) {
    $.ajax({
        url: "{% url 'api-part-list' %}",
        data: {
            {% if category %}
            'category': {{ category.id }},
            {% endif %}
            'search': text
        },
        success: function(result) {
            $("#part-list").find("tr:gt(0)").remove();
            $.each(result.results, function(i, part) {
                add_part(part);
            })
        }
    });
}


$("#part-filter").keyup(function(e) {
    if (e.keyCode == 27){ // Escape key
        cancelTimer();
        $("#part-filter").val('');
    }
    else {
        var value = $(this).val().toLowerCase();

        delay(function() {
            filter_parts(value);
        }, 500);
    }
});

$("#clear-filter").click(function(){
    clearTimeout(keyDelay);
    $("#company-filter").val('');
    filter_parts('');
});

filter_parts('');

</script>