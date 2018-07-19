<?php
   $secretKey="testing";
   // here is code to check rights + cookies (warlock)
   // gen.

   //$rand=random_int(); /// PHP 7 use IT !!!!!
   $rand=rand();
   $time=time();
   $oper_id=10; // from COOKIE
   $sign=sha1($rand.$time.$oper_id.$secretKey);
   $token=base64_encode("$rand.$time.$oper_id.$sign");
   print $token;
   
