<h1 class="title">Pozdravljeni na strani kriptovalut. Na voljo vam je:</h1>
<form action="iskanje/" method="get">
<input type="text" name="naslov" value="" />
<input type="submit" value="Išči">
</form>

<ul>
% for kriptovaluta,kratica,leto in kriptovalute:
    <li>
        <a>
            {{kriptovaluta}}({{kratica}}), Leto ustanovitve: {{leto}} 
        </a>
    </li>
