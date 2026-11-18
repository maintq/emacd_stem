#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re

LEVEL_META = [
    {
        "folder": "1. Kindergarten",
        "level": "Mầm non",
        "name": "Mầm non (Kindergarten)",
        "age": "3 - 5 tuổi",
        "icon": "🌱",
        "desc": "Khám phá thế giới quan qua các giác quan, đồ chơi vận động và hiện tượng tự nhiên gần gũi."
    },
    {
        "folder": "2. Primary School",
        "level": "Tiểu học",
        "name": "Tiểu học (Primary School)",
        "age": "6 - 11 tuổi (Lớp 1 - 5)",
        "icon": "🎒",
        "desc": "Thực hành khoa học sáng tạo, chế tạo mô hình STEM thực tế và rèn luyện tư duy đặt câu hỏi."
    },
    {
        "folder": "3. Middle School",
        "level": "THCS",
        "name": "THCS (Middle School)",
        "age": "11 - 15 tuổi (Lớp 6 - 9)",
        "icon": "🔬",
        "desc": "Phân tích bản chất vật lý, cơ chế hoạt động máy móc, kỹ thuật tự động hóa và thuật toán cơ bản."
    },
    {
        "folder": "4. High School",
        "level": "THPT",
        "name": "THPT (High School)",
        "age": "15 - 18 tuổi (Lớp 10 - 12)",
        "icon": "🚀",
        "desc": "Thực hiện dự án kỹ thuật chuyên sâu, lập trình vi điều khiển, năng lượng tái tạo và giải pháp thực tiễn."
    }
]

# Educational knowledge base for generating high quality STEM content
TOPIC_KNOWLEDGE = {
    # Vietnamese topics
    "Khoa học vật lý": {
        "icon": "⚡",
        "desc": "Tìm hiểu về các định luật chuyển động, lực, áp suất và các dạng năng lượng trong đời sống.",
        "theory": "Khoa học vật lý giúp chúng ta giải thích cách thế giới xung quanh vận hành: từ trọng lực giữ chân ta trên mặt đất, năng lượng đàn hồi của dây cao su, đến nguyên lý đòn bẩy và ròng rọc giúp nâng vật nặng nhẹ nhàng.",
        "practice": [
            {"term": "Thế năng đàn hồi (Elastic Potential Energy)", "phonetic": "/ɪˈlæstɪk pəˈtɛnʃəl ˈɛnərdʒi/", "definition": "Năng lượng được tích trữ khi vật bị biến dạng đàn hồi như lò xo hoặc dây cao su.", "example": "Dây cao su bị kéo căng giữ thế năng đàn hồi để phóng xe đồ chơi."},
            {"term": "Động năng (Kinetic Energy)", "phonetic": "/kɪˈnɛtɪk ˈɛnərdʒi/", "definition": "Năng lượng mà một vật có được nhờ vào chuyển động của nó.", "example": "Xe đua chạy càng nhanh thì động năng của nó càng lớn."},
            {"term": "Lực ma sát (Friction Force)", "phonetic": "/ˈfrɪkʃən fɔːrs/", "definition": "Lực cản trở chuyển động xuất hiện tại bề mặt tiếp xúc giữa hai vật thể.", "example": "Lốp xe cao su có rãnh giúp tăng ma sát để xe không bị trượt."},
            {"term": "Định luật bảo toàn năng lượng", "phonetic": "/lɔː əv kɒnsərˈveɪʃən əv ˈɛnərdʒi/", "definition": "Năng lượng không tự nhiên sinh ra hay mất đi, mà chỉ chuyển hóa từ dạng này sang dạng khác.", "example": "Thế năng của dây cao su chuyển hóa thành động năng và một phần nhiệt năng do ma sát."}
        ],
        "quiz": [
            {
                "question": "Khi bạn xoay trục bánh xe để kéo căng dây cao su của xe đua, bạn đang tích lũy dạng năng lượng nào?",
                "options": ["Động năng", "Thế năng đàn hồi", "Năng lượng nhiệt", "Năng lượng hóa học"],
                "answer": "Thế năng đàn hồi",
                "explanation": "Khi dây cao su bị xoắn hoặc kéo căng, công cơ học được chuyển thành thế năng đàn hồi tích trữ bên trong nó."
            },
            {
                "question": "Yếu tố nào sau đây sẽ làm giảm ma sát giữa bánh xe và mặt đường phẳng?",
                "options": ["Bề mặt đường gồ ghề hơn", "Bôi trơn trục quay bằng dầu nhớt", "Tăng thêm trọng lượng của xe", "Dùng bánh xe có nhiều gai nhám"],
                "answer": "Bôi trơn trục quay bằng dầu nhớt",
                "explanation": "Chất bôi trơn tạo lớp đệm làm giảm sự tiếp xúc trực tiếp giữa các bề mặt kim loại, giảm lực cản ma sát."
            },
            {
                "question": "Tại sao xe đua dây cao su lại dừng lại sau khi chạy được một đoạn?",
                "options": ["Hết thế năng và lực ma sát cản trở chuyển động", "Trọng lực không còn tác dụng", "Động năng biến thành thế năng đàn hồi", "Khối lượng của xe tăng lên"],
                "answer": "Hết thế năng và lực ma sát cản trở chuyển động",
                "explanation": "Khi dây cao su nhả hết năng lượng, lực ma sát và sức cản không khí sẽ dần triệt tiêu động năng của xe."
            }
        ]
    },
    "Lực và chuyển động": {
        "icon": "🏎️",
        "desc": "Khám phá các loại lực: lực đẩy, lực kéo, lực hấp dẫn và mối quan hệ với gia tốc.",
        "theory": "Mọi vật thể chỉ thay đổi vận tốc hoặc hướng chuyển động khi có một lực tác dụng lên nó. Hiểu về các định luật chuyển động giúp các kỹ sư thiết kế phương tiện giao thông an toàn và hiệu quả.",
        "practice": [
            {"term": "Lực đẩy và Lực kéo (Push & Pull Forces)", "phonetic": "/pʊʃ ænd pʊl fɔːrsɪz/", "definition": "Tác động của một vật lên vật khác làm thay đổi trạng thái chuyển động hoặc hình dạng.", "example": "Đẩy chiếc hộp về phía trước hoặc kéo chiếc xe kéo."},
            {"term": "Quán tính (Inertia)", "phonetic": "/ɪˈnɜːrʃə/", "definition": "Xu hướng của một vật giữ nguyên trạng thái đứng yên hoặc chuyển động thẳng đều.", "example": "Khi xe buýt phanh gấp, hành khách có xu hướng chúi người về phía trước."},
            {"term": "Gia tốc (Acceleration)", "phonetic": "/əkˌsɛləˈreɪʃən/", "definition": "Đại lượng đo mức độ biến thiên vận tốc của vật theo thời gian.", "example": "Xe thể thao tăng tốc từ 0 lên 100 km/h trong 3 giây."}
        ],
        "quiz": [
            {
                "question": "Khi bạn ngồi trên xích đu và muốn chuyển động, bạn cần tạo ra lực nào?",
                "options": ["Lực đẩy hoặc lực kéo", "Chỉ lực hút từ trường", "Không cần lực nào", "Lực tĩnh điện"],
                "answer": "Lực đẩy hoặc lực kéo",
                "explanation": "Để thay đổi trạng thái đứng yên, ta cần một ngoại lực tác dụng thông qua lực đẩy chân hoặc kéo xích đu."
            },
            {
                "question": "Hiện tượng hành khách bị ngả về phía sau khi xe bắt đầu tăng tốc đột ngột là do hiện tượng gì?",
                "options": ["Quán tính", "Lực ma sát", "Lực đẩy Archimedes", "Sức căng bề mặt"],
                "answer": "Quán tính",
                "explanation": "Do quán tính, cơ thể hành khách có xu hướng giữ nguyên trạng thái đứng yên ban đầu khi xe tăng tốc."
            }
        ]
    },
    "Thiết kế công trình và kiến trúc": {
        "icon": "🏛️",
        "desc": "Học cách thiết kế kết cấu cầu, tháp cao tầng, mái vòm và khả năng chịu lực tối hạn.",
        "theory": "Kết cấu tam giác (truss) là kết cấu hình học bền vững nhất trong xây dựng. Các kỹ sư ứng dụng hình tam giác để xây dựng cầu treo, tháp truyền hình và các tòa nhà chọc trời chịu được gió bão và động đất.",
        "practice": [
            {"term": "Tải trọng tới hạn (Critical Load)", "phonetic": "/ˈkrɪtɪkəl loʊd/", "definition": "Lực nén tối đa mà một kết cấu hoặc cột trụ có thể chịu đựng trước khi bị oằn hoặc sụp đổ.", "example": "Trọng tải tối đa mà cây cầu que kem có thể nâng đỡ trước khi gãy."},
            {"term": "Kết cấu giàn tam giác (Truss Structure)", "phonetic": "/trʌs ˈstrʌktʃər/", "definition": "Hệ thống các thanh liên kết tạo thành các tam giác giúp phân tán lực đều khắp công trình.", "example": "Mái nhà và các cây cầu thép luôn có dạng giàn tam giác."},
            {"term": "Trọng tâm (Center of Gravity)", "phonetic": "/ˈsɛntər əv ˈɡrævəti/", "definition": "Điểm đặt của trọng lực tác dụng lên toàn bộ vật thể.", "example": "Tòa tháp có đáy rộng và trọng tâm thấp sẽ đứng vững hơn."}
        ],
        "quiz": [
            {
                "question": "Hình học nào sau đây có tính ổn định và chống biến dạng chịu lực tốt nhất trong kiến trúc?",
                "options": ["Hình chữ nhật", "Hình tam giác", "Hình tròn", "Hình lục giác"],
                "answer": "Hình tam giác",
                "explanation": "Hình tam giác có cấu trúc cố định cả 3 góc khi chịu lực, phân tán tải trọng đều sang các cạnh mà không bị xô lệch."
            },
            {
                "question": "Để một tòa tháp mô hình bằng que kem đứng vững và không bị đổ khi có gió, kỹ sư nên thiết kế như thế nào?",
                "options": ["Chân đế rộng và trọng tâm đặt thấp", "Đỉnh tháp nặng hơn chân đế", "Tháp càng hẹp ở đáy càng tốt", "Chỉ dùng một cột chống thẳng đứng"],
                "answer": "Chân đế rộng và trọng tâm đặt thấp",
                "explanation": "Chân đế rộng cùng trọng tâm thấp làm tăng diện tích tiếp xúc và độ thăng bằng ổn định của kết cấu."
            }
        ]
    },
    "Lập trình và khoa học máy tính": {
        "icon": "💻",
        "desc": "Khám phá thế giới mã lệnh: HTML, thuật toán giải mê cung, mã vạch và logic máy tính.",
        "theory": "Máy tính xử lý thông tin thông qua các thuật toán (các bước hướng dẫn logic tuần tự). Ngôn ngữ lập trình là cầu nối giúp con người truyền đạt yêu cầu để máy tính thực hiện các tác vụ phức tạp một cách chính xác.",
        "practice": [
            {"term": "Thuật toán (Algorithm)", "phonetic": "/ˈælɡəˌrɪðəm/", "definition": "Tập hợp các bước chỉ dẫn có thứ tự rõ ràng để giải quyết một bài toán cụ thể.", "example": "Thuật toán bám tường tay phải để thoát khỏi mê cung."},
            {"term": "Mã nhị phân (Binary Code)", "phonetic": "/ˈbaɪnəri koʊd/", "definition": "Hệ thống biểu diễn dữ liệu bằng hai chữ số 0 và 1 mà máy tính hiểu được.", "example": "Chữ cái 'A' được lưu trữ dưới dạng mã nhị phân 01000001."},
            {"term": "Thẻ HTML (HTML Tag)", "phonetic": "/ˌeɪtʃ tiː ɛm ˈɛl tæɡ/", "definition": "Phần tử định dạng cấu trúc nội dung trên trang web như văn bản, hình ảnh, liên kết.", "example": "Thẻ <h1> định nghĩa tiêu đề chính của trang web."}
        ],
        "quiz": [
            {
                "question": "Đâu là thuật toán kinh điển đơn giản nhất để robot tự tìm đường thoát khỏi một mê cung kín?",
                "options": ["Đi ngẫu nhiên không mục đích", "Quy tắc bám theo tường tay phải (hoặc tay trái)", "Nhảy qua tường mê cung", "Đứng yên đợi bản đồ"],
                "answer": "Quy tắc bám theo tường tay phải (hoặc tay trái)",
                "explanation": "Quy tắc bám tường tay phải đảm bảo robot duyệt liên tục các lối đi và sẽ dẫn tới lối ra nếu mê cung liên thông."
            },
            {
                "question": "Ngôn ngữ nào sau đây được sử dụng để xây dựng khung xương cấu trúc của một trang web?",
                "options": ["HTML", "Photoshop", "MP3", "USB"],
                "answer": "HTML",
                "explanation": "HTML (HyperText Markup Language) là ngôn ngữ đánh dấu chuẩn dùng để tạo nên cấu trúc nền tảng của mọi trang web."
            }
        ]
    },
    "Năng lượng xanh": {
        "icon": "🌱",
        "desc": "Khai thác sức mạnh từ tự nhiên: pin năng lượng mặt trời, cối xay gió, đập thủy điện.",
        "theory": "Năng lượng tái tạo (mặt trời, gió, nước) là nguồn năng lượng sạch không thải ra khí nhà kính, giúp bảo vệ Trái Đất và tạo ra nguồn điện bền vững cho tương lai nhân loại.",
        "practice": [
            {"term": "Quang điện (Photovoltaic)", "phonetic": "/ˌfoʊtoʊvɑːlˈteɪɪk/", "definition": "Hiện tượng biến đổi trực tiếp năng lượng ánh sáng mặt trời thành năng lượng điện.", "example": "Tấm pin mặt trời trên mái nhà sạc pin cho bình ắc quy."},
            {"term": "Tua bin gió (Wind Turbine)", "phonetic": "/wɪnd ˈtɜːrbaɪn/", "definition": "Thiết bị chuyển đổi động năng của gió thành cơ năng rồi thành điện năng.", "example": "Cánh quạt gió quay khi có gió thổi mạnh làm quay máy phát điện."},
            {"term": "Thủy điện (Hydroelectricity)", "phonetic": "/ˌhaɪdroʊɪˌlɛkˈtrɪsɪti/", "definition": "Điện năng được tạo ra từ thế năng và động năng của dòng nước chảy từ trên cao.", "example": "Đập thủy điện xả nước làm quay tua bin phát điện."}
        ],
        "quiz": [
            {
                "question": "Tấm pin năng lượng mặt trời biến đổi dạng năng lượng nào thành điện năng?",
                "options": ["Nhiệt năng", "Năng lượng ánh sáng", "Năng lượng hóa học", "Năng lượng âm thanh"],
                "answer": "Năng lượng ánh sáng",
                "explanation": "Hiệu ứng quang điện trong các tế bào bán dẫn giúp chuyển đổi các hạt photon ánh sáng thành dòng điện một chiều."
            },
            {
                "question": "Tại sao năng lượng mặt trời và năng lượng gió được gọi là năng lượng tái tạo?",
                "options": ["Vì chúng không bao giờ cạn kiệt trong tự nhiên", "Vì giá thành rất đắt", "Vì chúng sinh ra nhiều khói bụi", "Vì chỉ dùng được vào ban đêm"],
                "answer": "Vì chúng không bao giờ cạn kiệt trong tự nhiên",
                "explanation": "Ánh sáng mặt trời và gió liên tục được thiên nhiên bổ sung nên không bị cạn kiệt như nhiên liệu hóa thạch."
            }
        ]
    },
    "Điện và mạch điện": {
        "icon": "💡",
        "desc": "Tìm hiểu về dòng điện, mạch nối tiếp, mạch song song và các linh kiện cơ bản.",
        "theory": "Dòng điện là dòng chuyển dời có hướng của các hạt mang điện (electron). Để một bóng đèn phát sáng, ta cần một nguồn điện (pin), dây dẫn và một mạch điện khép kín.",
        "practice": [
            {"term": "Mạch nối tiếp (Series Circuit)", "phonetic": "/ˈsɪriz ˈsɜːrkɪt/", "definition": "Mạch điện trong đó các thiết bị được nối liên tiếp thành một đường dẫn duy nhất.", "example": "Nếu một bóng đèn trong mạch nối tiếp bị đứt, toàn bộ mạch sẽ ngắt."},
            {"term": "Mạch song song (Parallel Circuit)", "phonetic": "/ˈpærəlɛl ˈsɜːrkɪt/", "definition": "Mạch điện có nhiều nhánh rẽ độc lập cho dòng điện chạy qua.", "example": "Đèn trong nhà được mắc song song để bật tắt độc lập."},
            {"term": "Chất dẫn điện và Chất cách điện", "phonetic": "/kənˈdʌktər ænd ˈɪnsəleɪtər/", "definition": "Chất dẫn điện cho dòng điện đi qua (đồng, nhôm); chất cách điện ngăn dòng điện (nhựa, cao su).", "example": "Lõi dây điện bằng đồng bọc vỏ nhựa cách điện an toàn."}
        ],
        "quiz": [
            {
                "question": "Điều gì xảy ra nếu tháo một bóng đèn trong mạch điện mắc nối tiếp?",
                "options": ["Các đèn còn lại sáng hơn", "Tất cả các đèn còn lại đều tắt", "Mạch điện phát nổ", "Không có thay đổi gì"],
                "answer": "Tất cả các đèn còn lại đều tắt",
                "explanation": "Trong mạch nối tiếp chỉ có một đường đi duy nhất cho dòng điện. Khi một linh kiện hở, mạch bị ngắt hoàn toàn."
            },
            {
                "question": "Vật liệu nào sau đây là chất dẫn điện tốt nhất?",
                "options": ["Thước kẻ nhựa", "Dây đồng", "Miếng gỗ khô", "Găng tay cao su"],
                "answer": "Dây đồng",
                "explanation": "Kim loại đồng chứa nhiều electron tự do giúp dẫn truyền dòng điện rất hiệu quả."
            }
        ]
    },
    "Bảo vệ môi trường": {
        "icon": "🌍",
        "desc": "Công nghệ xử lý rác thải, tái chế giấy, làm sạch vết dầu loang và bảo vệ đại dương.",
        "theory": "Bảo vệ môi trường bằng kỹ thuật STEM bao gồm việc sáng tạo các thiết bị phân loại rác tự động, vật liệu thấm hút dầu sinh học và quy trình tái chế tuần hoàn giảm thiểu rác thải nhựa.",
        "practice": [
            {"term": "Tái chế (Recycling)", "phonetic": "/ˌriːˈsaɪklɪŋ/", "definition": "Quy trình chuyển đổi vật liệu phế thải thành các sản phẩm mới có ích.", "example": "Tái chế giấy báo cũ thành vở viết và bìa carton."},
            {"term": "Vết dầu loang (Oil Spill)", "phonetic": "/ɔɪl spɪl/", "definition": "Sự cố dầu tràn ra biển gây ô nhiễm nghiêm trọng cho hệ sinh thái đại dương.", "example": "Kỹ sư dùng phao quây và vật liệu xốp kỵ nước để thu gom dầu tràn."},
            {"term": "Phân loại rác (Waste Sorting)", "phonetic": "/weɪst ˈsɔːrtɪŋ/", "definition": "Tách riêng rác hữu cơ, rác vô cơ và rác tái chế để xử lý hiệu quả.", "example": "Dùng nam châm để tự động hút kim loại ra khỏi băng chuyền rác."}
        ],
        "quiz": [
            {
                "question": "Phương pháp vật lý nào thường được dùng trên băng chuyền để tự động tách vỏ lon sắt ra khỏi rác tái chế?",
                "options": ["Dùng nam châm điện hút sắt", "Dùng quạt thổi bay sắt", "Dùng nước ngâm cho sắt tan", "Đốt nóng chảy sắt"],
                "answer": "Dùng nam châm điện hút sắt",
                "explanation": "Sắt có tính từ tính mạnh nên nam châm điện có thể dễ dàng hút và tách sắt ra khỏi các loại rác phi kim loại."
            },
            {
                "question": "Tại sao dầu nổi trên mặt nước khi xảy ra sự cố tràn dầu trên biển?",
                "options": ["Dầu có khối lượng riêng nhỏ hơn nước biển", "Dầu nặng hơn nước biển", "Dầu bị nước hòa tan hoàn toàn", "Dầu có màu đen"],
                "answer": "Dầu có khối lượng riêng nhỏ hơn nước biển",
                "explanation": "Dầu mỏ nhẹ hơn nước và kỵ nước (không tan trong nước) nên tạo thành một lớp váng nổi trên bề mặt."
            }
        ]
    },
    "Hàng không vũ trụ": {
        "icon": "🚀",
        "desc": "Nguyên lý bay, khí động học, tên lửa nước và công nghệ hàng không.",
        "theory": "Máy bay và tên lửa bay được nhờ định luật 3 Newton (lực tác dụng và phản lực) cùng lực nâng khí động học tạo ra bởi hình dạng cánh khí động học (airfoil).",
        "practice": [
            {"term": "Lực nâng khí động học (Aerodynamic Lift)", "phonetic": "/ˌɛroʊdaɪˈnæmɪk lɪft/", "definition": "Lực hướng lên trên vuông góc với dòng khí do chênh lệch áp suất quanh cánh máy bay.", "example": "Cánh máy bay cong phía trên giúp tạo lực nâng nâng cả chiếc máy bay nặng hàng tấn."},
            {"term": "Phản lực (Reaction Force / Thrust)", "phonetic": "/ˈriːˈækʃən fɔːrs/", "definition": "Lực đẩy tiến về phía trước sinh ra khi khí hoặc nước phụt mạnh về phía sau.", "example": "Tên lửa nước bay vút lên cao nhờ nước phụt ngược xuống dưới áp suất khí nén."}
        ],
        "quiz": [
            {
                "question": "Tên lửa nước bay lên cao dựa trên nguyên lý vật lý cơ bản nào?",
                "options": ["Định luật III Newton: Lực và phản lực", "Lực đẩy Archimedes", "Sự dẫn nhiệt", "Từ trường Trái Đất"],
                "answer": "Định luật III Newton: Lực và phản lực",
                "explanation": "Khí nén đẩy nước phụt mạnh xuống đất (hành động), tạo ra phản lực đẩy thân tên lửa vút lên trời."
            }
        ]
    },
    "Vận tải": {
        "icon": "🚡",
        "desc": "Hệ thống băng tải công nghiệp, dây chuyền lắp ráp, cáp treo và ròng rọc.",
        "theory": "Hệ thống vận tải cơ khí sử dụng ròng rọc, dây đai và bánh răng để truyền lực và giảm công cơ học khi vận chuyển hàng hóa và con người.",
        "practice": [
            {"term": "Hệ thống cáp treo (Cable Car System)", "phonetic": "/ˈkeɪbəl kɑːr ˈsɪstəm/", "definition": "Hệ thống vận tải dùng dây cáp kéo cabin vượt qua địa hình dốc đứng hoặc thung lũng.", "example": "Cáp treo leo núi giúp du khách lên đỉnh đồi dễ dàng."},
            {"term": "Ròng rọc (Pulley)", "phonetic": "/ˈpʊli/", "definition": "Bánh xe có rãnh để luồn dây, giúp thay đổi hướng của lực hoặc giảm lực kéo.", "example": "Ròng rọc động giúp giảm một nửa lực nâng cần thiết."}
        ],
        "quiz": [
            {
                "question": "Ròng rọc cố định mang lại lợi ích cơ học gì cho người thợ xây?",
                "options": ["Đổi hướng của lực kéo giúp kéo xuống dễ hơn nâng lên", "Giảm 10 lần trọng lượng của vật", "Tăng vận tốc của vật lên 100 lần", "Làm vật biến mất"],
                "answer": "Đổi hướng của lực kéo giúp kéo xuống dễ hơn nâng lên",
                "explanation": "Ròng rọc cố định không làm lợi về lực nhưng làm đổi hướng của lực kéo, cho phép người kéo dùng chính trọng lượng cơ thể để kéo vật lên."
            }
        ]
    },
    "Bảo tồn thế giới hoang dã": {
        "icon": "🐾",
        "desc": "Thiết kế cầu vượt sinh thái cho động vật, thiết bị cứu hộ và bảo vệ sinh thái.",
        "theory": "Con người phát triển hạ tầng giao thông thường chia cắt môi trường sống hoang dã. Kỹ sư môi trường thiết kế các hành lang sinh thái xanh (wildlife corridor) để động vật qua đường an toàn.",
        "practice": [
            {"term": "Cầu vượt sinh thái (Wildlife Overpass)", "phonetic": "/ˈwaɪldlaɪf ˈoʊvərˌpæs/", "definition": "Cây cầu phủ cỏ cây xây bắc qua đường cao tốc giúp động vật hoang dã di chuyển an toàn.", "example": "Cầu vượt cho gấu và hươu băng qua đường cao tốc xuyên rừng."},
            {"term": "Môi trường sống (Habitat)", "phonetic": "/ˈhæbɪtæt/", "definition": "Nơi cư trú tự nhiên cung cấp đầy đủ thức ăn, nước và nơi trú ẩn cho loài sinh vật.", "example": "Rừng nhiệt đới là môi trường sống đa dạng của hàng ngàn loài chim."}
        ],
        "quiz": [
            {
                "question": "Mục đích quan trọng nhất của việc xây dựng cầu vượt sinh thái qua đường cao tốc là gì?",
                "options": ["Ngăn tai nạn giao thông và bảo vệ lối di chuyển an toàn cho động vật", "Làm đẹp cho cảnh quan đường bộ", "Để xe ô tô chạy nhanh hơn", "Thu hút khách du lịch chụp ảnh"],
                "answer": "Ngăn tai nạn giao thông và bảo vệ lối di chuyển an toàn cho động vật",
                "explanation": "Cầu vượt sinh thái kết nối các mảng rừng bị chia cắt, giúp các loài thú hoang tìm thức ăn và bạn tình mà không bị xe đâm."
            }
        ]
    },
    # English topics
    "Force and Motion": {
        "icon": "🏎️",
        "desc": "Explore push and pull forces, kinetic vs potential energy, gravity, and Newton's laws.",
        "theory": "Forces make things speed up, slow down, or change direction. When you store energy in a stretched rubber band or spring, you create potential energy that turns into kinetic energy when released.",
        "practice": [
            {"term": "Potential Energy", "phonetic": "/pəˈtɛnʃəl ˈɛnərdʒi/", "definition": "Energy that is stored in an object due to its position or state.", "example": "A stretched rubber band stores elastic potential energy."},
            {"term": "Kinetic Energy", "phonetic": "/kɪˈnɛtɪk ˈɛnərdʒi/", "definition": "The energy an object has because of its motion.", "example": "A speeding toy car has high kinetic energy."},
            {"term": "Friction", "phonetic": "/ˈfrɪkʃən/", "definition": "The resistance that one surface encounters when moving over another.", "example": "Smooth wheels experience less friction on polished tiles."}
        ],
        "quiz": [
            {
                "question": "What type of energy is stored when you wind up the rubber band of a toy racer?",
                "options": ["Kinetic Energy", "Elastic Potential Energy", "Thermal Energy", "Electrical Energy"],
                "answer": "Elastic Potential Energy",
                "explanation": "Winding the rubber band stretches its polymer chains, storing energy as elastic potential energy until released."
            },
            {
                "question": "What force causes a rolling marble to eventually slow down and stop on the floor?",
                "options": ["Gravity alone", "Friction and air resistance", "Magnetism", "Centrifugal force"],
                "answer": "Friction and air resistance",
                "explanation": "Friction between the floor and the marble, along with air resistance, converts kinetic energy into tiny amounts of heat."
            }
        ]
    },
    "Programming and Computer Science": {
        "icon": "💻",
        "desc": "Learn how computers think: algorithms, binary logic, HTML, web design, and robotics.",
        "theory": "Computer Science is about problem solving. Programs are sets of instructions that tell hardware what to do. Learning HTML and computational thinking allows you to build the digital future.",
        "practice": [
            {"term": "Algorithm", "phonetic": "/ˈælɡəˌrɪðəm/", "definition": "A step-by-step procedure or set of rules for solving a problem.", "example": "A recipe or a maze-solving procedure is an algorithm."},
            {"term": "HTML Element", "phonetic": "/ˌeɪtʃ tiː ɛm ˈɛl ˈɛləmənt/", "definition": "The building block of a web page consisting of tags and content.", "example": "The <p> element creates a paragraph on a web page."},
            {"term": "Debugging", "phonetic": "/diːˈbʌɡɪŋ/", "definition": "The process of finding and resolving bugs or defects in software.", "example": "Checking your code line by line to fix an error."}
        ],
        "quiz": [
            {
                "question": "What is the primary role of HTML in web development?",
                "options": ["To store database records", "To define the structure and content of web pages", "To make computer hardware run faster", "To encrypt passwords"],
                "answer": "To define the structure and content of web pages",
                "explanation": "HTML (HyperText Markup Language) structures content into headings, paragraphs, images, and links."
            },
            {
                "question": "What do we call an ordered sequence of instructions used to solve a computational problem?",
                "options": ["An algorithm", "A monitor", "A microchip", "A firewall"],
                "answer": "An algorithm",
                "explanation": "An algorithm is a well-defined sequence of instructions that takes inputs and produces an expected output."
            }
        ]
    },
    "Green energy": {
        "icon": "☀️",
        "desc": "Harnessing renewable energy from the sun, wind, and flowing water for a clean planet.",
        "theory": "Renewable energy comes from natural sources that are constantly replenished. Solar panels convert sunlight into electricity, while wind turbines capture kinetic energy from moving air.",
        "practice": [
            {"term": "Solar Photovoltaic Cell", "phonetic": "/ˈsoʊlər ˌfoʊtoʊvɑːlˈteɪɪk sɛl/", "definition": "A semiconductor device that converts light directly into electrical power.", "example": "Solar panels on a roof provide clean electricity during sunny days."},
            {"term": "Renewable Resource", "phonetic": "/rɪˈnuːəbəl ˈriːsɔːrs/", "definition": "A natural source of energy that is not depleted by use, like wind or sun.", "example": "Wind energy is clean and inexhaustible."}
        ],
        "quiz": [
            {
                "question": "Which of the following is a key advantage of solar energy?",
                "options": ["Produces zero greenhouse gas emissions during operation", "Only works at midnight", "Creates toxic smoke while generating power", "Consumes fossil fuel"],
                "answer": "Produces zero greenhouse gas emissions during operation",
                "explanation": "Solar panels convert photon light directly into electrical energy without combustion or carbon emissions."
            }
        ]
    },
    "Architectural Design and Construction": {
        "icon": "🏗️",
        "desc": "Structural engineering, truss bridges, high-rise skyscrapers, and critical load testing.",
        "theory": "Civil engineers design bridges and towers that can support immense weight and resist winds. The triangular truss structure distributes tension and compression forces evenly.",
        "practice": [
            {"term": "Compression Force", "phonetic": "/kəmˈprɛʃən fɔːrs/", "definition": "A squeezing force that pushes materials together.", "example": "The pillars of a bridge are under strong compression."},
            {"term": "Tension Force", "phonetic": "/ˈtɛnʃən fɔːrs/", "definition": "A pulling force that stretches materials apart.", "example": "The suspension cables on the Golden Gate bridge are under tension."}
        ],
        "quiz": [
            {
                "question": "Why do engineers use triangular trusses in bridge and crane construction?",
                "options": ["Triangles cannot be deformed without bending one of their sides", "Triangles are lighter than single lines", "Triangles absorb magnetic fields", "It is only for decoration"],
                "answer": "Triangles cannot be deformed without bending one of their sides",
                "explanation": "Triangles provide geometric rigidity because their angles are fixed once the side lengths are set, distributing loads evenly."
            }
        ]
    },
    "Wildlife conservation": {
        "icon": "🦁",
        "desc": "Protecting endangered animals, building wildlife corridors, and preserving natural ecosystems.",
        "theory": "Wildlife conservation combines biology and engineering to monitor animal populations and build protective infrastructure like fish ladders and wildlife highway crossings.",
        "practice": [
            {"term": "Wildlife Corridor", "phonetic": "/ˈwaɪldlaɪf ˈkɔːrɪdɔːr/", "definition": "A strip of natural habitat connecting wildlife populations separated by human activities.", "example": "An overpass covered with native trees allows bears to cross highways."},
            {"term": "Ecosystem", "phonetic": "/ˈiːkoʊˌsɪstəm/", "definition": "A biological community of interacting organisms and their physical environment.", "example": "Coral reefs provide homes and nutrients for diverse marine life."}
        ],
        "quiz": [
            {
                "question": "How do wildlife bridges across highways help maintain biodiversity?",
                "options": ["They allow animals to travel safely to find food, mates, and shelter", "They attract cars to stop for photos", "They trap animals in cages", "They prevent trees from growing"],
                "answer": "They allow animals to travel safely to find food, mates, and shelter",
                "explanation": "Connecting fragmented habitats prevents inbreeding and vehicle collisions, helping wildlife populations thrive."
            }
        ]
    }
}

def clean_title_from_filename(filename):
    name = filename.replace('.pdf', '')
    # remove common prefixes
    for p in ['bai-giang-', 'eng-tg--', 'eng-tg-', 'eng-tg---', 'eng-', '[ENG] TG - ', '[ENG] TG-', '0022l-', '0018l-', '0026l-', '0028-L ', '0028l-']:
        if name.lower().startswith(p.lower()):
            name = name[len(p):]
    # replace hyphens, underscores
    name = name.replace('--', '-').replace('-', ' ').replace('_', ' ')
    name = re.sub(r'\s+', ' ', name).strip()
    return name.title()

def get_topic_info(topic_name, lang):
    # Match against known topics
    for k, v in TOPIC_KNOWLEDGE.items():
        if k.lower() in topic_name.lower() or topic_name.lower() in k.lower():
            return v
    
    # Generic fallback
    if lang == 'VIE':
        return {
            "icon": "📚",
            "desc": f"Khám phá kiến thức thực tế và bài tập thực hành về {topic_name}.",
            "theory": f"Chủ đề '{topic_name}' cung cấp cái nhìn thực tế và các phương pháp giải quyết vấn đề theo tư duy khoa học STEM. Học sinh sẽ làm quen với các khái niệm cốt lõi, quan sát mô hình và áp dụng vào chế tạo.",
            "practice": [
                {"term": f"Khái niệm cốt lõi ({topic_name})", "phonetic": "/kɒnˌsɛpt/", "definition": f"Kiến thức nền tảng giúp hiểu rõ nguyên lý hoạt động của {topic_name}.", "example": f"Ứng dụng nguyên lý {topic_name} trong các mô hình thực nghiệm."},
                {"term": "Quy trình thiết kế kỹ thuật (EDP)", "phonetic": "/ˌɛndʒɪˈnɪərɪŋ dɪˈzaɪn ˈprɑːsɛs/", "definition": "Quy trình lặp gồm: Xác định vấn đề -> Nghiên cứu -> Thiết kế -> Chế tạo thử nghiệm -> Đánh giá hoàn thiện.", "example": "Luôn thử nghiệm và cải tiến mô hình nhiều lần để đạt hiệu suất tốt nhất."}
            ],
            "quiz": [
                {
                    "question": f"Bước đầu tiên trong quy trình thiết kế kỹ thuật STEM khi nghiên cứu {topic_name} là gì?",
                    "options": ["Xác định rõ vấn đề và mục tiêu cần giải quyết", "Mua vật liệu đắt nhất", "Viết báo cáo kết quả trước", "Bỏ qua thử nghiệm"],
                    "answer": "Xác định rõ vấn đề và mục tiêu cần giải quyết",
                    "explanation": "Quy trình thiết kế kỹ thuật luôn khởi đầu bằng việc làm rõ nhu cầu thực tế và bài toán cần giải quyết."
                }
            ]
        }
    else:
        return {
            "icon": "🔬",
            "desc": f"Hands-on inquiry and STEM investigations in {topic_name}.",
            "theory": f"The topic '{topic_name}' engages learners in practical STEM methodology, combining scientific theory, engineering design, and critical analytical thinking.",
            "practice": [
                {"term": f"Core Concept ({topic_name})", "phonetic": "/kɔːr ˈkɑːnsɛpt/", "definition": f"Fundamental principle underpinning the study of {topic_name}.", "example": f"Applying {topic_name} principles to real-world engineering."},
                {"term": "Engineering Design Process (EDP)", "phonetic": "/ˌɛndʒɪˈnɪərɪŋ dɪˈzaɪn ˈprɑːsɛs/", "definition": "Iterative series of steps: Ask -> Imagine -> Plan -> Create -> Test -> Improve.", "example": "Engineers continuously prototype and test their solutions."}
            ],
            "quiz": [
                {
                    "question": f"What is the first step in the Engineering Design Process when exploring {topic_name}?",
                    "options": ["Define the problem and constraints", "Build the final product immediately", "Write the conclusion", "Skip testing"],
                    "answer": "Define the problem and constraints",
                    "explanation": "Engineers must clearly understand the challenge, user needs, and design constraints before planning a solution."
                }
            ]
        }

def build_complete_dataset():
    data = []
    
    for meta in LEVEL_META:
        folder = meta["folder"]
        if not os.path.isdir(folder):
            continue
            
        level_entry = {
            "level": meta["level"],
            "levelFullName": meta["name"],
            "levelFolder": folder,
            "ageGroup": meta["age"],
            "icon": meta["icon"],
            "description": meta["desc"],
            "languages": []
        }
        
        for lang in ["VIE", "ENG"]:
            lang_dir = os.path.join(folder, lang)
            if not os.path.isdir(lang_dir):
                continue
                
            lang_entry = {
                "lang": lang,
                "langName": "Tiếng Việt" if lang == "VIE" else "English",
                "topics": []
            }
            
            raw_topics = sorted([t for t in os.listdir(lang_dir) if os.path.isdir(os.path.join(lang_dir, t)) and not t.startswith('.')])
            
            for t_folder in raw_topics:
                t_path = os.path.join(lang_dir, t_folder)
                pdfs = sorted([f for f in os.listdir(t_path) if f.endswith('.pdf')])
                if not pdfs:
                    continue
                
                clean_topic_name = t_folder.strip()
                topic_info = get_topic_info(clean_topic_name, lang)
                
                topic_entry = {
                    "topicId": f"{meta['level']}-{lang}-{clean_topic_name}".replace(' ', '-').lower(),
                    "topicName": clean_topic_name,
                    "folder": t_folder,
                    "icon": topic_info.get("icon", "📚"),
                    "description": topic_info.get("desc", f"Học và thực hành {clean_topic_name}"),
                    "lectures": []
                }
                
                for idx, pdf in enumerate(pdfs, 1):
                    lec_title = clean_title_from_filename(pdf)
                    content_url = f"./{folder}/{lang}/{t_folder}/{pdf}"
                    thumb_slug = pdf.replace('.pdf', '')
                    thumb_url = f"./{folder}/{lang}/{t_folder}/thumb-{thumb_slug}.jpg"
                    video_url = f"./{folder}/{lang}/{t_folder}/video-{thumb_slug}.mp4"
                    audio_url = f"./{folder}/{lang}/{t_folder}/audio-{thumb_slug}.mp3"
                    
                    # Create lecture entry
                    lec_entry = {
                        "lectureId": f"L{idx:02d}",
                        "title": lec_title,
                        "fileName": pdf,
                        "contentUrl": content_url,
                        "thumbnailUrl": thumb_url,
                        "media": {
                            "videoUrl": video_url,
                            "audioUrl": audio_url
                        },
                        "theoryNotes": topic_info.get("theory", ""),
                        "practiceData": topic_info.get("practice", []),
                        "quizData": topic_info.get("quiz", [])
                    }
                    topic_entry["lectures"].append(lec_entry)
                
                lang_entry["topics"].append(topic_entry)
            
            level_entry["languages"].append(lang_entry)
        
        data.append(level_entry)
        
    return data

if __name__ == "__main__":
    dataset = build_complete_dataset()
    
    # Save as data.json
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    print("Successfully wrote data.json")
    
    # Save as data.js for seamless offline/file:// protocol execution
    js_content = "/**\n * E-Learning Resource Tree Mock Data\n * Mapped directly to internal directory structure:\n * Level -> Language -> Topic -> Lectures\n */\nwindow.APP_DATA = " + json.dumps(dataset, ensure_ascii=False, indent=2) + ";\n"
    with open("data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Successfully wrote data.js")
    
    # Print summary
    total_lectures = sum(len(t['lectures']) for lvl in dataset for lg in lvl['languages'] for t in lg['topics'])
    print(f"Total Levels: {len(dataset)}")
    print(f"Total Lectures mapped: {total_lectures}")
