{{extends file="layout.tpl"}}

{{block name="css"}}

{{/block}}

{{block name="js"}}

{{/block}}

{{block name="body"}}
  <div class="container">
    <h3 class="mx-2 mt-3">My Videos</h3>
    <div class="d-flex flex-wrap video-list">
      {{for $i=1 to 8}}
        <div class="card m-2">
          <img class="card-img-top" src="/assets/images/thumbnail-{{$i}}.jpeg" alt="Card image cap">
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <h5 class="card-title">Video - {{$i}}</h5>
              <span class="date">25/11/2018</span>
            </div>
            <a href="/search?id={{$i}}" class="btn btn-warning float-right mt-4">Search Inside</a>
          </div>
        </div>
      {{/for}}
    </div>
  </div>
{{/block}}
