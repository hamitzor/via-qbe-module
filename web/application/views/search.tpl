{{extends file="layout.tpl"}}

{{block name="css"}}

{{/block}}

{{block name="js"}}

{{/block}}

{{block name="body"}}
  <div class="container px-2 py-3">
    <h3>Search Inside {{$model.name}}</h3>
    <form enctype="multipart/form-data" action="/search_submit" method="post">
      <input type="hidden" name="id" value="{{$model.id}}">
      <div class="form-group">
        <label for="exampleFormControlFile1">Upload an image to search inside the video</label>
        <input type="file" name="example" class="form-control-file">

        <button class="btn btn-success my-4" type="submit">Start Search Proccess</button>
      </div>
    </form>
  </div>
{{/block}}
