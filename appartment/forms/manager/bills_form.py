from django import forms
from appartment.models.bills import Bill


class BillForm(forms.ModelForm):
    # Sử dụng widget để có ô chọn tháng/năm thân thiện hơn
    bill_month = forms.DateField(
        widget=forms.DateInput(attrs={"type": "month"}), label="Tháng của hóa đơn"
    )

    class Meta:
        model = Bill
        # Liệt kê các trường mà người dùng sẽ nhập liệu
        fields = [
            "room",
            "bill_month",
            "electricity_amount",
            "water_amount",
            "additional_service_amount",
            "total_amount",  # Tạm thời cho phép nhập tay, sẽ cải tiến sau
            "status",
            "due_date",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Định nghĩa các lớp CSS chung cho các loại input
        text_input_class = "mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md shadow-sm"

        # Lặp qua tất cả các trường trong form để thêm class
        for field_name, field in self.fields.items():
            # Thêm class chung cho tất cả
            field.widget.attrs.update({"class": text_input_class})

        # Tùy chỉnh riêng cho các trường đặc biệt nếu cần
        # Ví dụ: thay đổi widget cho bill_month và due_date
        self.fields["bill_month"].widget = forms.DateInput(
            attrs={
                "type": "text",  # Đổi thành text để tránh xung đột với picker mặc định
                "class": f"{text_input_class} month-picker",  # Thêm class mới
                "placeholder": "Chọn tháng và năm",
            }
        )
        self.fields["due_date"].widget = forms.DateInput(
            attrs={"type": "date", "class": text_input_class}
        )
