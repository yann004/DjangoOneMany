$(document).ready(function() {
    $('.toggle-books').click(function() {
        $(this).siblings('.book-list').toggleClass('hidden');
    });
});

