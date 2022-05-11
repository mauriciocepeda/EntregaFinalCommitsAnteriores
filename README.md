# Entrega1CEPEDA

Buenas tardes Matias, paso a detallarte como diseñe la web.

Es mas o menos lo que veniamos trabajando en clase, la web consta de una app con 3 modelos: ALUMNO, PROFESOR Y CURSO(esta ultima fue la que elegi para que se pueda buscar en la base de datos, de todas maneras esta indicada en la web con un DANGER BUTTON)

el trabajo cuenta con herencia de templates: una plantilla padre, un html para cada modelo donde se pueden cargar mas objetos, una plantilla de busqueda, y una plantilla para los resultados de la busqueda. todas las paginas estan "identadas" por los buttons del menu.

para probar la web primero recomiendo cargar algunos objetos desde la misma, en el orden que se desee, y luego corroborarlos desde el admin de django (el nombre del superuser que cree es "mauri" y la contraseña 123456, no se si es solo a modo local o se mantiene cuando comparto el archivo, por las dudas te lo digo) o corroborarlos desde la misma web en caso de que sean del modelo CURSO.

Por ultimo, con lo que respecta a CURSOS, la pagina que nos dirige cuando pulsamos el boton del menu es al de cargar modelos. debajo del formulario hay otro boton de BUSCAR CURSOS, que al apretarlo nos redidrige a una pagina de busqueda, donde pdodremos buscar los objetos que se han cargado POR NOMBRE. si no se ingrese ningun nombre o se ingresa uno que no existe en la base de datos, la plantilla de resultados de busqueda no lo hara saber. 

