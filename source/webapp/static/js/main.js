async function makeRequest(url, method = 'GET') {
    let response = await fetch(url, {method})

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }

}

async function onClick(event) {
    event.preventDefault();
    let link = event.target;
    console.log(link);
    let url = link.href;
    let data = await makeRequest(url);
    console.log(data);
    let span = document.getElementById(data.id);
    span.innerText = data.test;
    span.innerText += data.comments_count;
}

function onLoad() {
    let links = document.getElementsByClassName('article_link');
    for (let link of links) {
        link.addEventListener('click', onClick);
    }
}


window.addEventListener('load', onLoad);