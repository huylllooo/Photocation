function loadData() {

    var cityStr = $('#city').val();

    _500px.init({
        sdk_key: '263c9111787193d930ce0aa02f6e353ed5928fad'	//replace with your js sdk key
    });

    // Get my user id
    _500px.api('/photos/search', { term: cityStr, page: 1 }, function(response) {
        console.log(response.data.photos);
        var siteurl = "http://500px.com/photo/";
        if (response.success) {
            $.each(response.data.photos, function() {
                $('#grid').append('<article class="post col-md-2 col-sm-2 col-xs-12 panel panel-default"><h3>' + '</h3><a href="' + siteurl + this.id + '" target="_blank"><img src="' + this.image_url + '" /></a></article>');
            });
        } else {
            alert('Nothing found! Please refresh...');
        }
    });

    return false;
};

$('#form-container').submit(loadData);