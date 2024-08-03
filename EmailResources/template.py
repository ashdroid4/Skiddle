"""This is the template file where you add your html and body"""

# An example has been done for you!

html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en" style="font-family:'Exo 2', sans-serif">
 <head>
  <meta charset="UTF-8">
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta content="telephone=no" name="format-detection">
  <title>New Message</title><!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    </style>
    <![endif]--><!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--><!--[if gte mso 9]>
<xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG></o:AllowPNG>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
</xml>
<![endif]--><!--[if !mso]><!-- -->
  <link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet"><!--<![endif]-->
  <style type="text/css">
.rollover span {
	font-size:0;
}
.container-hover:hover>table {
	background:linear-gradient(153.06deg, #7EE8FA -0.31%, #EEC0C6 99.69%)!important;
	transition:0.3s all!important;
}
.es-menu.es-table-not-adapt td a:hover,
a.es-button:hover {
	text-decoration:underline!important;
}
#outlook a {
	padding:0;
}
.es-button {
	mso-style-priority:100!important;
	text-decoration:none!important;
}
a[x-apple-data-detectors] {
	color:inherit!important;
	text-decoration:none!important;
	font-size:inherit!important;
	font-family:inherit!important;
	font-weight:inherit!important;
	line-height:inherit!important;
}
.es-desk-hidden {
	display:none;
	float:left;
	overflow:hidden;
	width:0;
	max-height:0;
	line-height:0;
	mso-hide:all;
}
@media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150%!important } h1, h2, h3, h1 a, h2 a, h3 a { line-height:120%!important } h1 { font-size:28px!important; text-align:left } h2 { font-size:24px!important; text-align:left } h3 { font-size:20px!important; text-align:left } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:28px!important; text-align:left } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:24px!important; text-align:left } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px!important; text-align:left } .es-menu td a { font-size:16px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:16px!important } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:16px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:inline-block!important } a.es-button, button.es-button { font-size:20px!important; display:inline-block!important } .es-adaptive table, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0!important } .es-m-p0r { padding-right:0!important } .es-m-p0l { padding-left:0!important } .es-m-p0t { padding-top:0!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } tr.es-desk-hidden { display:table-row!important } table.es-desk-hidden { display:table!important } td.es-desk-menu-hidden { display:table-cell!important } .es-menu td { width:1%!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } .es-m-p5 { padding:5px!important } .es-m-p5t { padding-top:5px!important } .es-m-p5b { padding-bottom:5px!important } .es-m-p5r { padding-right:5px!important } .es-m-p5l { padding-left:5px!important } .es-m-p10 { padding:10px!important } .es-m-p10t { padding-top:10px!important } .es-m-p10b { padding-bottom:10px!important } .es-m-p10r { padding-right:10px!important } .es-m-p10l { padding-left:10px!important } .es-m-p15 { padding:15px!important } .es-m-p15t { padding-top:15px!important } .es-m-p15b { padding-bottom:15px!important } .es-m-p15r { padding-right:15px!important } .es-m-p15l { padding-left:15px!important } .es-m-p20 { padding:20px!important } .es-m-p20t { padding-top:20px!important } .es-m-p20r { padding-right:20px!important } .es-m-p20l { padding-left:20px!important } .es-m-p25 { padding:25px!important } .es-m-p25t { padding-top:25px!important } .es-m-p25b { padding-bottom:25px!important } .es-m-p25r { padding-right:25px!important } .es-m-p25l { padding-left:25px!important } .es-m-p30 { padding:30px!important } .es-m-p30t { padding-top:30px!important } .es-m-p30b { padding-bottom:30px!important } .es-m-p30r { padding-right:30px!important } .es-m-p30l { padding-left:30px!important } .es-m-p35 { padding:35px!important } .es-m-p35t { padding-top:35px!important } .es-m-p35b { padding-bottom:35px!important } .es-m-p35r { padding-right:35px!important } .es-m-p35l { padding-left:35px!important } .es-m-p40 { padding:40px!important } .es-m-p40t { padding-top:40px!important } .es-m-p40b { padding-bottom:40px!important } .es-m-p40r { padding-right:40px!important } .es-m-p40l { padding-left:40px!important } .m-c-p16r { padding-right:8vw } .es-desk-hidden { display:table-row!important; width:auto!important; overflow:visible!important; max-height:inherit!important } }
@media screen and (max-width:384px) {.mail-message-content { width:414px!important } }
</style>
 </head>
 <body style="width:100%;font-family:'Exo 2', sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
  <div dir="ltr" class="es-wrapper-color" lang="en" style="background-color:#12022F"><!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" src="https://fnhsopx.stripocdn.email/content/guids/CABINET_bf3f28777a864b4fca3f15706a2554aa/images/group_10.png" color="#12022f" origin="0.5, 0" position="0.5, 0"></v:fill>
			</v:background>
		<![endif]-->
   <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" background="https://fnhsopx.stripocdn.email/content/guids/CABINET_bf3f28777a864b4fca3f15706a2554aa/images/group_10.png" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-image:url(https://fnhsopx.stripocdn.email/content/guids/CABINET_bf3f28777a864b4fca3f15706a2554aa/images/group_10.png);background-repeat:no-repeat;background-position:center top;background-color:#12022F" role="none">
     <tr>
      <td valign="top" style="padding:0;Margin:0">
       <table cellpadding="0" cellspacing="0" class="es-content" align="center" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
         <tr>
          <td class="es-m-p15r es-m-p15l" align="center" style="padding:0;Margin:0">
           <table class="es-content-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:640px" role="none">
             <tr>
              <td class="es-m-p20" align="left" bgcolor="#ffffff" style="Margin:0;padding-top:30px;padding-bottom:40px;padding-left:40px;padding-right:40px;background-color:#ffffff;border-radius:20px 20px 0px 0px">
               <table cellpadding="0" cellspacing="0" width="100%" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                 <tr>
                  <td align="left" style="padding:0;Margin:0;width:560px">
                   <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                     <tr>
                      <td align="left" style="padding:0;Margin:0;font-size:0px" height="32"><a target="_blank" href="https://ashagency.site" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#391484;font-size:18px"><img class="adapt-img" src="https://fnhsopx.stripocdn.email/content/guids/CABINET_484636efc2f93c122deb90bdbb62f5e0b19638930e5f0056d2270d5f8aa58201/images/ashagencyhighresolutionlogotransparent.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="230" height="32"></a></td>
                     </tr>
                     <tr>
                      <td align="left" style="padding:0;Margin:0;padding-top:30px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><strong>Hello,</strong></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><br></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px">Are you struggling to close deals despite having a solid product or service? 😕 Are your sales strategies not delivering the expected results, leaving potential revenue on the table? 💸</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><br></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px">At Ash Agency, I specialize in creating tailored offers that resonate with your target audience and significantly boost your conversion rates. Even though I'm just starting out, my innovative approach is designed to help businesses like yours turn prospects into loyal customers. 💼✨</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><br></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px">For the next 10 clients, I am offering my services completely free of charge. 🎁 After this limited-time offer, my service will be priced at only 10% of the revenue I help you generate. This means you only pay when you see results! 💰✅</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><br></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px">Without implementing a powerful offer strategy, you may continue to face low conversion rates and missed revenue opportunities. 🚫 Your competitors might pull ahead, leaving you struggling to catch up. 🏃‍♂️</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><br></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px">Imagine consistently closing deals and watching your revenue grow exponentially. 📈 With my expertise, you'll have a compelling offer that attracts and converts your ideal customers, giving you a competitive edge in the market. 🏆<br type="_moz"></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><br></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px">This offer is a no-brainer, and you can see how quickly I can secure 10 clients. Don’t miss out on this exclusive opportunity! Be one of the first 10 clients to experience my services for free and transform your sales strategy today. DM me on Facebook, Instagram, or reply to this email to get started immediately. 📬</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><br></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><strong>Regards,<br type="_moz"></strong></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><strong>Ashutosh Biswal</strong></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><strong>CEO</strong></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:27px;color:#666666;font-size:18px"><strong>Ashagency</strong></p></td>
                     </tr>
                     <tr>
                      <td align="left" style="padding:0;Margin:0;padding-top:25px"><!--[if mso]><a href="https://ashagency.site" target="_blank" hidden>
	<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" esdevVmlButton href="https://ashagency.site" 
                style="height:52px; v-text-anchor:middle; width:186px" arcsize="50%" strokecolor="#ffdda9" strokeweight="2px" fillcolor="#ffdda9">
		<w:anchorlock></w:anchorlock>
		<center style='color:#000000; font-family:"Exo 2", sans-serif; font-size:20px; font-weight:400; line-height:20px;  mso-text-raise:1px'>Learn More</center>
	</v:roundrect></a>
<![endif]--><!--[if !mso]><!-- --><span class="msohide es-button-border" style="border-style:solid;border-color:#FFDDA9;background:#FFDDA9;border-width:0px 0px 2px 0px;display:inline-block;border-radius:30px;width:auto;mso-hide:all"><a href="https://ashagency.site" class="es-button" target="_blank" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#000000;font-size:20px;padding:15px 30px 15px 30px;display:inline-block;background:#FFDDA9;border-radius:30px;font-family:'Exo 2', sans-serif;font-weight:normal;font-style:normal;line-height:24px;width:auto;text-align:center;mso-padding-alt:0;mso-border-alt:10px solid #FFDDA9">Learn More</a></span><!--<![endif]--></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
             <tr>
              <td class="es-m-p20" align="left" bgcolor="#f9f9f9" style="padding:40px;Margin:0;background-color:#f9f9f9;border-radius:0px 0px 20px 20px">
               <table cellpadding="0" cellspacing="0" width="100%" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                 <tr>
                  <td align="left" style="padding:0;Margin:0;width:560px">
                   <table cellpadding="0" cellspacing="0" width="100%" bgcolor="#f9f9f9" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;background-size:initial;background-attachment:initial;background-origin:initial;background-clip:initial;background-color:#f9f9f9;border-radius:20px" role="none">
                     <tr>
                      <td style="padding:0;Margin:0">
                       <table width="100%" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                         <tr>
                          <td valign="top" style="padding:0;Margin:0;width:64px">
                           <table role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                             <tr>
                              <td align="center" style="padding:0;Margin:0;display:none"></td>
                             </tr>
                           </table></td>
                          <td style="padding:0;Margin:0;width:20px"></td>
                          <td valign="top" style="padding:0;Margin:0">
                           <table width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                             <tr>
                              <td style="padding:0;Margin:0"><h3 class="p_name" style="Margin:0;line-height:24px;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;font-size:20px;font-style:normal;font-weight:normal;color:#000000"><b>Ashutosh Biswal</b></h3></td>
                             </tr>
                             <tr>
                              <td align="left" style="padding:0;Margin:0;padding-top:5px"><h5 style="Margin:0;line-height:120%;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;color:#666666">CEO, Ash Agency<br></h5></td>
                             </tr>
                             <tr>
                              <td align="left" style="padding:0;Margin:0;padding-top:10px;font-size:0">
                              <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                              <tr>
                              <td align="center" valign="top" style="padding:0;Margin:0;padding-right:15px"><a target="_blank" href="https://www.facebook.com/profile.php?id=100092966106031" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#391484;font-size:18px"><img title="Facebook" src="https://fnhsopx.stripocdn.email/content/assets/img/social-icons/logo-colored/facebook-logo-colored.png" alt="Fb" width="24" height="24" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></a></td>
                              <td align="center" valign="top" style="padding:0;Margin:0"><a target="_blank" href="https://instagram.com/ashty_drone" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#391484;font-size:18px"><img title="Instagram" src="https://fnhsopx.stripocdn.email/content/assets/img/social-icons/logo-colored/instagram-logo-colored.png" alt="Inst" width="24" height="24" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></a></td>
                              </tr>
                              </table></td>
                             </tr>
                           </table></td>
                         </tr>
                       </table></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
           </table></td>
         </tr>
       </table>
       <table cellpadding="0" cellspacing="0" class="es-content" align="center" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
         <tr>
          <td align="center" style="padding:0;Margin:0">
           <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:640px">
             <tr>
              <td align="left" style="padding:40px;Margin:0">
               <table cellpadding="0" cellspacing="0" width="100%" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                 <tr>
                  <td align="center" valign="top" style="padding:0;Margin:0;width:560px">
                   <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                     <tr>
                      <td align="center" height="0" style="padding:0;Margin:0"></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
           </table></td>
         </tr>
       </table>
       <table cellpadding="0" cellspacing="0" class="es-footer" align="center" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top">
         <tr>
          <td class="es-m-p15r es-m-p15l" align="center" style="padding:0;Margin:0">
           <table class="es-footer-body" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:640px" role="none">
             <tr>
              <td align="left" bgcolor="#ffffff" style="padding:40px;Margin:0;background-color:#ffffff;border-radius:20px">
               <table cellpadding="0" cellspacing="0" width="100%" role="none" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                 <tr>
                  <td class="es-m-p40b" align="center" valign="top" style="padding:0;Margin:0;width:560px">
                   <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                     <tr>
                      <td align="center" class="es-m-p35r es-m-txt-c" style="padding:0;Margin:0;font-size:0px" height="30"><a target="_blank" href="https://viewstripo.email/" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#391484;font-size:16px"><img src="https://fnhsopx.stripocdn.email/content/guids/CABINET_484636efc2f93c122deb90bdbb62f5e0b19638930e5f0056d2270d5f8aa58201/images/ashagencyhighresolutionlogotransparent.png" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="128" height="18"></a></td>
                     </tr>
                     <tr>
                      <td align="center" style="padding:0;Margin:0;padding-top:20px;font-size:0">
                       <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                         <tr>
                          <td align="center" valign="top" style="padding:0;Margin:0;padding-right:15px"><a target="_blank" href="https://www.facebook.com/profile.php?id=100092966106031" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#391484;font-size:16px"><img title="Facebook" src="https://fnhsopx.stripocdn.email/content/assets/img/social-icons/logo-colored-bordered/facebook-logo-colored-bordered.png" alt="Fb" width="32" height="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></a></td>
                          <td align="center" valign="top" style="padding:0;Margin:0"><a target="_blank" href="https://instagram.com/ashty_drone" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#391484;font-size:16px"><img title="Instagram" src="https://fnhsopx.stripocdn.email/content/assets/img/social-icons/logo-colored-bordered/instagram-logo-colored-bordered.png" alt="Inst" width="32" height="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></a></td>
                         </tr>
                       </table></td>
                     </tr>
                     <tr>
                      <td align="center" style="padding:0;Margin:0;padding-top:15px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:24px;color:#666666;font-size:16px">Tulsipur, Cuttack, Odisha, India,<br type="_moz"></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:24px;color:#666666;font-size:16px">753008<br type="_moz"></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:24px;color:#666666;font-size:16px"><br type="_moz"></p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:24px;color:#666666;font-size:16px">© 2024 Ash Agency. All rights reserved.<br type="_moz"></p></td>
                     </tr>
                     <tr>
                      <td align="center" style="padding:0;Margin:0;padding-top:10px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:'Exo 2', sans-serif;line-height:24px;color:#333333;font-size:16px">This is a cold email. To unsubscribe, email to <u><a target="_blank" href="mailto:unsubscribe@ashagency.site?subject=Unsubscribe me from Cold Emails." style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#391484;font-size:16px">unsubscribe@ashagency.site</a></u>, even though you won't be getting this email ever again.<br type="_moz"></p></td>
                     </tr>
                   </table></td>
                 </tr>
               </table></td>
             </tr>
           </table></td>
         </tr>
       </table></td>
     </tr>
   </table>
  </div>
 </body>
</html>
'''

body = ''' 
Hello,

Are you struggling to close deals despite having a solid product or service? 😕 Are your sales strategies not delivering the expected results, leaving potential revenue on the table? 💸

At Ash Agency, I specialize in creating tailored offers that resonate with your target audience and significantly boost your conversion rates. Even though I'm just starting out, my innovative approach is designed to help businesses like yours turn prospects into loyal customers. 💼✨

For the next 10 clients, I am offering my services completely free of charge. 🎁💯 After this limited-time offer, my service will be priced at only 10% of the revenue I help you generate. This means you only pay when you see results! 💰✅

Without implementing a powerful offer strategy, you may continue to face low conversion rates and missed revenue opportunities. 🚫❌ Your competitors might pull ahead, leaving you struggling to catch up. 🏃‍♂️💨

Imagine consistently closing deals and watching your revenue grow exponentially. 📈💹 With my expertise, you'll have a compelling offer that attracts and converts your ideal customers, giving you a competitive edge in the market. 🏆💪

This offer is a no-brainer, and you can see how quickly I can secure 10 clients. 🤩 Don’t miss out on this exclusive opportunity! Be one of the first 10 clients to experience my services for free and transform your sales strategy today. DM me on Facebook, Instagram, or reply to this email to get started immediately. 📬✉️

Best regards,
Ashutosh Biswal
CEO
Ash Agency
'''
