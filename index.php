<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="./public/css/login.css">
    <title>Login</title>
</head>
<body>
    <form class="text-center" style="width: 300px;">
        <img class="mb-4" src="./public/img/log.jpeg" alt="" width="72" height="72">
        <h1 class="h3 mb-3 font-weight-normal">Por favor inicia sesión</h1>
        <label for="inputuser" class="sr-only">Usuario</label>
        <input type="name" id="inputEmail" class="form-control mb-3" placeholder="Usuario" required autofocus>
        <label for="inputPassword" class="sr-only">Contraseña</label>
        <input type="password" id="inputPassword" class="form-control mb-3" placeholder="Contraseña" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Iniciar sesión</button>
    </form>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>
</html>
