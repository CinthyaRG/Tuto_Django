$("#id_submit").click(function () {
      var first_name = $(this).val();
      alert("HOLA");

      $.ajax({
          url:'http://localhost:8001/router/usuarios/',
          data: {first_name:'Cinthya',
              last_name:'Ramos',
              email: '123@re.ee'
          },
          type:'POST',
          dataType: 'json',
          success: function (data) {
              document.write("EXITO JSON")
          },
          error: function (data) {
              document.write("ERROR JSON")
          }
      });
});




