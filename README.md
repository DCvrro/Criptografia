# Criptografia

El siguiente repositorio, corrsponde a TODO EL LABORATORIO 2 DE CRIPTOGRAFIA, relacionado a PASSWORDS. 

Lo solicitado fue: 

Hito I
Cada estudiante deberá utilizar Dorks (búsquedas avanzadas), para encontrar leaks(Filtraciones) de credenciales de usuario relacionados a páginas Chilenas. Este Dork usado, deberá entregar un máximo de 5 resultados relacionados a la búsqueda solicitada. Las URLs que contengan las credenciales, deberán ser ingresadas en un excel compartido  donde éstas, no podrán repetirse. Para completar este hito, deberán conseguirse 20 credenciales de usuarios relacionadas a páginas Chilenas, las cuales serán usadas en la segunda parte de esta actividad. Asimismo, se exige a el/la estudiante, elegir 2 sitios web , uno Chileno y otro perteneciente a la Unión Europea, que permita registro de usuarios, recordar contraseña e inicio de sesión. Todos estos datos deben ingresarse en el Excel Compartido.

 

Hito II
La segunda entrega tendrá como objetivo, probar si efectivamente estos sitios que fueron vulnerados tomaron acciones, con lo cual se corroborará si las credenciales encontradas funcionan en la plataforma. Para ello, se deberá automatizar los inicios de sesión para cada sitio mediante un script en el lenguaje de programación de su preferencia o herramientas de ataques de fuerza bruta (p.e: Medusa (Enlaces a un sitio externo.) , THC-Hydra (Enlaces a un sitio externo.) , Patator  (Enlaces a un sitio externo.), entre otros). Sólo sitios que posean un control de Captcha o similar, podrán hacerse de forma manual, pero deberá ser mencionado en el reporte final tanto la metodología, como las herramientas usadas para dicho propósito.

Este hito se considerará completo al presentar la automatización exitosa durante el horario de clases. En caso de existir mecanismos de control de automatizaciones, se deberá presentar el procedimiento utilizado para probar las credenciales encontradas.

Hito III
En este Hito, el/la estudiante deberá auditar la implementación de los sistemas de creación, actualización, acceso, transmisión y recuperación de contraseñas de 2 los dos sitios elegidos en los hitos anteriores (uno de uso exclusivo para usuarios chilenos y uno para usuarios pertenecientes a la comunidad europea), automatizando el proceso mediante el uso del lenguaje de programación a su elección.

Para esto, deberá implementar un código en el lenguaje que usted estime conveniente, para automatizar lo siguiente:

Creación de una cuenta
Inicio de sesión (permitirá hacer ataques por fuerza bruta contra su cuenta de usuario).
Restablecimiento de contraseña (no requiere login del usuario).
Modificación de contraseña (requiere login del usuario).
El hito se contará como completo al presentar el código desarrollado, funcionando y cumpliendo cada una de las automatizaciones solicitadas.

Hito IV
En este Hito, el/la estudiante deberá contestar las siguientes preguntas, las cuales deberán agregarse al informe final.

¿Cuál es el largo (L) mínimo y máximo de la contraseña a utilizar? ¿Cuál es la máxima base (W) que permite utilizar el sitio? Debe probar con las 6 bases que están a continuación:
Unicode (https://en.wikipedia.org/wiki/List_of_Unicode_characters (Enlaces a un sitio externo.))
Superscripts and subscripts:  ₁ⁱₕ₉ₘ₊⁼⁽ₔ⁰.
Emojis (https://unicode.org/Public/emoji/ (Enlaces a un sitio externo.)): V. 1.0: 🌝💓😢🙉,  V. 14.0: ☔⛄👏🏿❤️.
ASCII 256: @#~¥§«Æ¼ñÑá^ø=()’\($þ”ßÐ‡‰―‼⁊‹¢
Base62: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
Alfabetos (https://www.alphabet-type.com/tools/charset-builder/ (Enlaces a un sitio externo.)):  Arabic: ؛ ڜ ﭗ ﺹ ﻇ ﻨ ﻩ ﻲ
El largo mínimo/máximo está restringido desde el cliente? En caso de ser así, intente deshabilitar el límite de la contraseña y verifique si el servidor permite registrarse con una contraseña de un mayor tamaño. En caso de no poder, indique porqué no lo logró.
¿Existe comprobación de robustez de la contraseña al momento de registrarse? En caso de ser así, intente deshabilitar esta opción y verifique si el servidor acepta el uso de contraseñas débiles. En caso de no poder, indique porqué no lo logró.
¿Se transmite la contraseña en texto plano?
¿En qué variable se transmite al servidor el usuario y contraseña? (Variable utilizada en GET o POST, no en el HTML)
¿Qué información se solicita para restablecer la contraseña?
¿Cómo opera el servicio de restablecer contraseña? (se envía la existente, se crea una temporal o el usuario reinicia la antigua por una nueva)
¿En el proceso de reinicia se expone información privada del usuario? ¿La información expuesta está completa o de forma parcial (n***@gmail.com)?
En caso de generar una contraseña temporal. ¿Qué patrón tiene la nueva contraseña al reiniciarla? Automatice 10 reinicios de la contraseña (utilizando el proceso c) para obtener el patrón de las nuevas contraseñas, representado por una expresión regular. La extracción de las contraseñas nuevas que le lleguen al correo electrónico o celular, lo puede hacer de forma manual.
¿El sitio recuerda contraseñas antiguas? ¿Cuántas? ¿Es posible eliminar esas contraseñas de la memoria del servidor (se pueden sobrescribir)? 
¿Las políticas del usuario obligan a entregar información verdadera? Verifique si el sitio obliga a ingresar su segundo apellido. En caso de ser así, ¿Qué podría hacer un usuario que solo tenga uno, sin tener que falsificar sus datos?
¿El sitio es susceptible a ataques por fuerza bruta? ¿Cómo lo evita? Pruebe automatizando 100 accesos (recuerde que su cuenta se podría inhabilitar o bloquear, por lo que deberá realizar este proceso al final y no a última hora)
¿Existe la opción de eliminar su cuenta? En caso de ser así, ¿Queda algún indicio de la existencia de su cuenta? Para verificar si existe algún indicio de la cuenta se puede realizar lo siguiente:  Volver a registrarse con los mismos datos, o ir repitiendo datos (en distintas cuentas) para determinar cuáles se van guardando, Recuperar la contraseña.
¿Los resultados obtenidos se condicen con las políticas de privacidad y seguridad del sitio?
 

Su código deberá ser subido a la plataforma GitHub, y adjuntar el link en el informe, el cual deberá ser subido a Canvas en formato PDF a más tardar la fecha indicada. Además, deberá completar el excel (Enlaces a un sitio externo.) con los sitios a auditar, junto a la información recopilada

Recuerde revisar si el dominio que usted eligió estaba previamente en el excel. En el caso que existan 2 alumnos que auditaron el mismo sitio, se evaluará sólo al que lo eligió primero (se verificará con el sistema de versionamiento de gdocs).

Cualquier duda que tenga sobre el informe pregunte por el foro de Canvas. 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Adenmas, se generó un informe, que se encuentra en la carpta LAB2, en donde se explica todo lo desarrollado. 

El canal de Youtube donde se respaldo toda la informacion es el siguiente: 
https://www.youtube.com/channel/UCk5pfvIDquP594yWTGmUN7g/videos

Ante cualquier duda o informacion, solicitar contacto. 
