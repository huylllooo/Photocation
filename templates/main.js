function loadData() {

    var cityStr = $('#city').val();
    $('.grid').innerHTML = "";
    _500px.init({
        sdk_key: '263c9111787193d930ce0aa02f6e353ed5928fad' //replace with your js sdk key
    });

    // Append photo with buttons to html
    _500px.api('/photos/search', { term: cityStr, image_size: 4, page: 1 }, function(response) {
        //console.log(response.data.photos);
        var siteurl = "http://500px.com/photo/";
        var mapUrl = "https://www.google.com/maps/@";
        if (response.success) {
            $.each(response.data.photos, function() {
                // Check if location available
                if (this.latitude && this.longitude) {
                    $('.grid').append('<div class="grid-item contain"><h5>' + '</h5><img src="'+ this.image_url + '" class="image" width="99%"/>' +
                        '<form class="middle">'+
                            '<div class="text glyphicon glyphicon-map-marker"><a href="https://www.google.co.jp/maps/?q=' + this.latitude + ',' + this.longitude + '" target="_blank"> Map</a></div>'+
                            '{% if logged_in %}'+
                            '<div class="text glyphicon glyphicon-save"><a href="' + siteurl + this.id + '" target="_blank"> 500px</a></div>'+
                            '{% else %}'+
                            '<div class="text glyphicon glyphicon-save"><a href="{{url_for("photoSite")}}"> 500px</a></div>'+
                            '{% endif %}'+
                        '</form>'+
                        '</div>');
                } else {
                    $('.grid').append('<div class="grid-item contain"><h5>' + '</h5><img src="'+ this.image_url + '" class="image" width="99%"/>' +
                        '<form class="middle">'+
                            '{% if logged_in %}'+
                            '<div class="text glyphicon glyphicon-save"><a href="' + siteurl + this.id + '" target="_blank"> 500px</a></div>'+
                            '{% else %}'+
                            '<div class="text glyphicon glyphicon-save"><a href="{{url_for("photoSite")}}"> 500px</a></div>'+
                            '{% endif %}'+
                        '</form>'+
                        '</div>');
                }

            });
        } else {
            alert('Nothing found! Please refresh...');
        }
    });

    return false;
};

$('#form-container').submit(loadData);