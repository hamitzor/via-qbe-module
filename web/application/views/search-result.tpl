{{extends file="layout.tpl"}}

{{block name="css"}}

{{/block}}

{{block name="js"}}

{{/block}}

{{block name="body"}}
  <div class="container px-2 py-3">
    <h3>Search results for search inside {{$model.name}} <span class="time-found">(12.3 Seconds)</span></h3>
    <h5>Example used for search</h5>
    <img class="searched-example mb-4" src="/assets/images/thumbnail-1.jpeg">

    {{if false}}
      <div class="alert alert-danger" role="alert">
        Example never occurs
      </div>
    {{else}}
      <div class="alert alert-success" role="alert">
        Example occurs 10 times
      </div>
      <table class="table table-hover ">
        <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Time</th>
          <th scope="col">Top Left Point</th>
          <th scope="col">Bottom Right Point</th>
        </tr>
        </thead>
        <tbody>
        {{for $i = 1 to 10}}
          <tr>
            <th scope="row">3</th>
            <td>Larry the Bird</td>
            <td>Larry the Bird</td>
            <td>@twitter</td>
          </tr>
        {{/for}}
        </tbody>
      </table>
    {{/if}}

    <a role="button" href="/search?id={{$model.id}}" class="btn btn-warning my-4">Search With Another Example</a>
  </div>
{{/block}}
