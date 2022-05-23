function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function onLikePublicationButtonClick(obj) {
    let is_liked = obj.target.attributes.getNamedItem('data-is-liked').value;
    let publication_id = obj.target.attributes.getNamedItem('data-id').value;
    is_liked = is_liked === "0" ? 0 : 1;
    let opts = {
        method: is_liked ? 'delete' : 'post',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json;charset=utf-8',
            'session_id': getCookie('session_id'),
            'mode': 'same-origin'
        },
        body: JSON.stringify({
            publication_id: publication_id,
        })
    };

    fetch('/api/v1/likes', opts).then((resp) => {
        if (resp.status === 200) {
            let old_src = obj.target.attributes.getNamedItem('src').value;
            obj.target.parentElement.children[1].children[0].innerHTML = parseInt(obj.target.parentElement.children[1].children[0].innerHTML) + (is_liked ? -1 : 1);
            obj.target.src = obj.target.attributes.getNamedItem('data-src-other').value;
            obj.target.setAttribute("data-src-other", old_src);
            obj.target.setAttribute("data-is-liked", is_liked ? 0 : 1);
        } else {
            console.log('unsuccess!')
        }
    })
}

function onCommentFormSubmit(obj) {
    let text = obj.target.children[1].value.valueOf()
    obj.target.children[1].value = ''
    let opts = {
        method: 'post',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json;charset=utf-8',
            'session_id': getCookie('session_id'),
            'mode': 'same-origin'
        },
        body: JSON.stringify({
            text: text,
            publication: parseInt(obj.target.attributes['data-id'].value)
        })
    };
    fetch('/api/v1/comments', opts).then((resp) => {
        if (resp.status === 201) {
            let comment_html = '<div class="comment">\n' +
                '                    <p style="font-style: italic">Комментарий от <a href="' + USER_PROFILE_URL + '">' + USER_USERNAME + '</a>\n' +
                '                    </p>\n' +
                '                    <p class="comment-text">' + text + '</p>\n' +
                '                </div>'
            if (obj.target.parentElement.children[0].children[0].id === 'no-comment-text')
                obj.target.parentElement.children[0].children[0].remove()
            obj.target.parentElement.children[0].insertAdjacentHTML('beforeend', comment_html)
        }
    })
    return false;
}

let commentForms = document.querySelectorAll('[id=comment-form]');
for (let btn_index in commentForms) {
    let form = commentForms[btn_index];
    try {
        form.onsubmit = onCommentFormSubmit
    } catch (e) {
    }
}


let publicationLikeButtons = document.getElementsByClassName('like-button');
for (let btn_index in publicationLikeButtons) {
    let btn = publicationLikeButtons[btn_index];
    try {
        btn.addEventListener('click', onLikePublicationButtonClick)
    } catch (e) {

    }
}
