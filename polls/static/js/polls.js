/**
 * Created by Troy on 2/11/2017.
 */

$.ajax({
    url : '/perform/acts/update/{{  act.id  }}/',
    type : "POST",
    data : {
        'csrfmiddlewaretoken' : "{{  csrf_token  }}",
        furtherData : furtherData
    },
    success : function(result) {}
});


$("#user_scores").change(function () {
  var str = "";
  $("#user_scores option:selected").each(function () {
        str += $(this).text() + ",";
      });
  $.ajax({
  type: "POST",
  url: "base.html",
  data: { values: str }
}).done(function( msg ) {
  alert( "Data Saved: " + msg );
});
})
.trigger('change');


window.location.reload(true);