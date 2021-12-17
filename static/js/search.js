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
        try {
            document.getElementById('results').innerHTML = "";
        } catch (e) {
            // Create the results container
            const results = document.createElement('ul');
            results.id = 'results';
            results.classList.add('list-reset', 'h-full', 'block');
            resultContainer.appendChild(results);
        }
        for (var result of results) {
            const listElement = document.createElement('li');
            listElement.classList.add('flex', 'items-center', 'space-x-2', 'py-2', 'px-4', 'relative', 'w-full', 'hover:bg-blue-600', 'hover:text-white', 'cursor-pointer');
            listElement.setAttribute('latitude', result.item.latitude);
            listElement.setAttribute('longitude', result.item.longitude);
            listElement.setAttribute('cityId', result.item.cityId);
            listElement.innerHTML = `<span class="text-sm font-semibold">${result.item.city}</span>`;
            listElement.addEventListener('click', (e) => {
                citySearch.removeAttribute('data-city-id');
                citySearch.value = e.target.innerText;
                citySearch.setAttribute('data-city-id', e.target.getAttribute('cityId'));
                citySearch.setAttribute('data-latitude', e.target.getAttribute('latitude'));
                citySearch.setAttribute('data-longitude', e.target.getAttribute('longitude'));
                resultContainer.classList.add('hidden');
                resultContainer.innerHTML = "";
                city = {
                    city: e.target.innerText,
                    latitude: e.target.getAttribute('latitude'),
                    longitude: e.target.getAttribute('longitude')
                };
                reRenderMap(city);
                document.getElementById('rangeContainer').classList.add('hidden');
                $rangeInput = $('.range input');
                $rangeInput.val(1).trigger('input');
            });
            document.getElementById('results').appendChild(listElement);
        }
    } else {
        document.getElementById('result_container').classList.add('hidden');
    }
});