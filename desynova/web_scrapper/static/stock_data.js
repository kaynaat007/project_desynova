
(function($) {
    $(document).ready(function() {

        // when page loads, call the function to load and display data
        loadData();
    });
})(jQuery);

// This functions makes ajax call to django backend and retrieves latest data in json
function loadData(){

   // fetch whatever is there in options value
   type = $('#choice').val();

   // change this to your server base address
   var base_url = 'http://localhost:8000';

   // make the url
   var url = base_url + '/web-scrapper/gainer-loser-data/?type='+type ;

   // call the api and fetch the data
   $.getJSON( url, function(data) {

        // construct the html dynamically
        main_html = '';
        $.each( data, function(index, single_card_data_object) {
             main_html += make_html_card(single_card_data_object);
        } );
        $('#card_root').html(main_html);
   }) ;

}

var sec = 120;

// This function runs every second. when number of seconds hit -1, a fresh call is made and sec is again set to 120 seconds.
var timer = setInterval(function() {
   $('#seconds').text(sec--);

   console.log(sec);

   if (sec == -1) {
      loadData(); // update the data as usual
      sec = 120; // set again sec equal to 60
      console.log("calling in next 1 minute");
   }
}, 1000);

// when user changes option from dropdown menu, again call the function and set sec = 120 seconds again
$('#choice').change(function(){

   // call again on change
   loadData();
   sec = 120; // update the sec again to 120 seconds.

});

// makes a single card html
function make_html_card(single_card_data_object) {

   html = '<div class="card"><div class="container">'
   heading = '<h4> <b> SYMBOL: </b> ' + single_card_data_object.symbol + '</h4> ';
   html += heading;

   $.each(single_card_data_object, function(key, value) {

          if ( key != "symbol") {
              element = '<p>' + key + ' : ' + value + '</p>';
              html += element;
          }
   } );

   html += '</div> </div>  <br/>';
   return html;

}