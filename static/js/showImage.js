// A $( document ).ready() block.
$( document ).ready(function() {
    const image = document.getElementById("image_decode")
    image.addEventListener('change', (e) => {
        let reader = new FileReader();
        // Leemos el archivo subido y se lo pasamos a nuestro fileReader
        reader.readAsDataURL(e.target.files[0]);

        // Le decimos que cuando este listo ejecute el código interno
        reader.onload = function(){
            let preview = document.getElementById('preview'),
            image = document.createElement('img');
            image.src = reader.result;
            preview.innerHTML = '';
            preview.append(image);
        };
    });

});
