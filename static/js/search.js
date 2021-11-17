const citySearch = document.getElementById('citySearch');
citySearch.addEventListener('keyup', (e) => {
    const fuse = new Fuse(cities, {
        keys: ['city'],
        threshold: 0.3,
    });
    const results = fuse.search(e.target.value);
    if (results.length > 0) {
        const resultContainer = document.getElementById('result_container');
        resultContainer.classList.remove('hidden');
        document.getElementById('results').innerHTML = "";
        for (var result of results) {
            const listElement = document.createElement('li');
            listElement.classList.add('flex', 'items-center', 'space-x-2', 'py-2', 'px-4', 'relative', 'w-full', 'hover:bg-blue-600', 'hover:text-white', 'cursor-pointer', 'resultCity');
            listElement.setAttribute('latitude', result.item.latitude);
            listElement.setAttribute('longitude', result.item.longitude);
            listElement.innerHTML = `<span class="text-sm font-semibold">${result.item.city}</span>`;
            listElement.addEventListener('click', (e) => {
                citySearch.value = e.target.innerText;
                resultContainer.classList.add('hidden');
                city = {
                    city: e.target.innerText,
                    latitude: e.target.getAttribute('latitude'),
                    longitude: e.target.getAttribute('longitude')
                };
                reRenderMap(city);
                console.log(city);
            });
            document.getElementById('results').appendChild(listElement);
        }
    } else {
        document.getElementById('result_container').classList.add('hidden');
    }
});