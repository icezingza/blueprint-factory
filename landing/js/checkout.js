// Stripe/PromptPay หรือ Hostinger Payment Button แบบง่าย
function pay(amountTHB){
  // ตัวอย่างใช้ Hostinger Payment Button (คุณต้องสร้าง button ใน panel ก่อน)
  // สมมติว่าคุณสร้าง payment link แล้วชื่อ btn_<amount>
  // ถ้าใช้ Stripe ให้เปลี่ยนเป็น Stripe Checkout Session
  window.open(`https://hostinger-payment-link/${amountTHB}?success=https://namonexus.com/landing/topup.html?paid=${amountTHB}&tx=HOSTINGER_TX`, '_blank');
}
