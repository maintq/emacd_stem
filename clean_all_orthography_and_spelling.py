#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

TITLE_MAP = {
    "T rọng tải tới hạn": "Trọng tải tới hạn",
    "Sử dụng ngôn ngữ H TML": "Sử dụng ngôn ngữ HTML",
    "Thử thách xây t oà tháp cao tầng": "Thử thách xây toà tháp cao tầng",
    "Đơn giản hóa độ phức tạp trong thuật t oán": "Đơn giản hóa độ phức tạp trong thuật toán",
    "Thiết kế dụng cụ cắt băng k eo": "Thiết kế dụng cụ cắt băng keo",
    "cây cầu từ que kem": "Cây cầu từ que kem",
    "Engineering Air T raffic": "Engineering Air Traffic",
    "T ake Flight!": "Take Flight!",
    "T all T ower Challenge": "Tall Tower Challenge",
    "Water T ower Challenge": "Water Tower Challenge",
    "W aterproof that Roof!": "Waterproof that Roof!",
    "Get Connected W ith Ohm's Law": "Get Connected With Ohm's Law",
    "Getting Y our Bearings": "Getting Your Bearings",
    "Cast your V ote": "Cast Your Vote",
    "Life V est Challenge": "Life Vest Challenge",
    "Nano W aterproofing": "Nano Waterproofing",
    "T ry Y our Hand at Nano": "Try Your Hand at Nano",
    "Pendulum T ime": "Pendulum Time",
    "T elescoping Periscope": "Telescoping Periscope",
    "T emperature T actics": "Temperature Tactics",
    "W riting in HTML": "Writing in HTML",
    "V anV oorhis": "Van Voorhis"
}

# Rich, curated STEM content for lessons that had OCR font issues
CURATED_LESSONS = {
    "Mạch nối tiếp và song song": {
        "theoryNotes": "Bài học này trình bày về các mạch điện đơn giản và sự khác nhau trong thiết kế và chức năng của các mạch nối tiếp và song song. Học sinh tìm hiểu về dòng điện, điện thế, tải tiêu thụ và cách thức hoạt động của công tắc.",
        "summary": "Bài học này trình bày về các mạch điện đơn giản và sự khác nhau trong thiết kế và chức năng của các mạch nối tiếp và song song. Học sinh tìm hiểu về dòng điện, điện thế, tải tiêu thụ và cách thức hoạt động của công tắc.",
        "scenario": "Nhóm em là các kỹ sư điện được giao nhiệm vụ thiết kế một hệ thống mạch điện chiếu sáng cho dãy phòng học. Hệ thống phải sử dụng công tắc điều khiển và đảm bảo nếu một bóng đèn bị tháo hoặc cháy hỏng thì các bóng đèn còn lại vẫn tiếp tục phát sáng bình thường.",
        "criteria": [
            "Phải vẽ sơ đồ và đấu nối thành công một mạch điện song song điều khiển nhiều bóng đèn.",
            "Mỗi bóng đèn phải sáng rõ và độc lập khi ngắt một nhánh tải."
        ],
        "constraints": [
            "Chỉ sử dụng những nguyên vật liệu được cung cấp (pin, dây dẫn, bóng đèn LED, công tắc).",
            "Đảm bảo tuyệt đối an toàn mạch, không xảy ra hiện tượng đoản mạch gây chập cháy."
        ]
    },
    "Cây cầu từ que kem": {
        "theoryNotes": "Bài học này hướng dẫn học sinh khám phá kỹ thuật kết cấu giàn (truss structure) và sức chịu tải của các dạng cầu trong kỹ thuật xây dựng. Học sinh sẽ nghiên cứu các lực tác động cơ bản gồm lực nén (compression) và lực kéo (tension), cách các thanh dầm tam giác phân tán trọng lực và chuyển tải trọng về các mố cầu hai bên.",
        "summary": "Bài học này hướng dẫn học sinh khám phá kỹ thuật kết cấu giàn (truss structure) và sức chịu tải của các dạng cầu trong kỹ thuật xây dựng. Học sinh sẽ nghiên cứu các lực tác động cơ bản gồm lực nén (compression) và lực kéo (tension), cách các thanh dầm tam giác phân tán trọng lực và chuyển tải trọng về các mố cầu hai bên.",
        "scenario": "Nhóm em là các kỹ sư cầu đường được giao nhiệm vụ thiết kế và thi công một mô hình cầu vượt qua một hẻm núi có khoảng cách 14 inch. Cây cầu phải sử dụng tối đa 200 que kem gỗ và keo dán, đạt khả năng chịu tải trọng lớn nhất có thể trước khi gãy đổ.",
        "criteria": [
            "Cầu phải chịu được tải trọng thử nghiệm tiêu chuẩn (từ 5 đến 20 pound / 2.3 đến 9 kg) đặt tại điểm giữa cầu trong tối thiểu 10 giây.",
            "Cấu trúc nhịp cầu phải đạt chiều dài tối thiểu 14 inch (khoảng 35 cm) và đủ rộng để xe mô hình đi qua."
        ],
        "constraints": [
            "Chỉ sử dụng tối đa 200 que kem gỗ và keo dán thủ công.",
            "Không được dán đặc toàn bộ thân cầu, phải thể hiện rõ các thanh giàn tam giác theo bản vẽ."
        ]
    },
    "Ròng rọc và lực căng dây": {
        "theoryNotes": "Bài học này hướng dẫn học sinh khám phá nguyên lý máy cơ đơn giản: ròng rọc cố định, ròng rọc động và hệ thống palăng (ròng rọc kép). Học sinh sẽ tìm hiểu về lợi ích cơ học (Mechanical Advantage), sự đánh đổi giữa lực kéo và quãng đường di chuyển của dây, cũng như lực căng dây (tension force) khi nâng vật nặng.",
        "summary": "Bài học này hướng dẫn học sinh khám phá nguyên lý máy cơ đơn giản: ròng rọc cố định, ròng rọc động và hệ thống palăng (ròng rọc kép). Học sinh sẽ tìm hiểu về lợi ích cơ học (Mechanical Advantage), sự đánh đổi giữa lực kéo và quãng đường di chuyển của dây, cũng như lực căng dây (tension force) khi nâng vật nặng.",
        "scenario": "Nhóm em là các kỹ sư cơ khí được giao thử thách thiết kế một hệ thống ròng rọc nâng vật liệu xây dựng lên cao tại công trường. Thử thách yêu cầu chế tạo một cơ cấu palăng cho phép một công nhân có thể nâng khối tải trọng nặng với lực kéo nhẹ nhất và độ an toàn cao nhất.",
        "criteria": [
            "Hệ thống ròng rọc phải nâng được vật nặng quy định lên độ cao tối thiểu 20 cm.",
            "Lực kéo đo được trên lực kế lò xo phải giảm ít nhất 50% so với khi nâng trực tiếp mà không dùng ròng rọc động."
        ],
        "constraints": [
            "Chỉ sử dụng các nguyên vật liệu được cung cấp (ròng rọc, dây dù mảnh, móc treo, quả cân, lực kế).",
            "Hệ thống phải vận hành êm ái, dây không bị trượt khỏi rãnh ròng rọc trong quá trình kéo."
        ]
    },
    "“Phiêu” cùng dù lượn": {
        "theoryNotes": "Bài học này tập trung vào kỹ thuật hàng không vũ trụ và động lực học chất lưu: lực cản không khí (drag), lực nâng khí động học (lift) và trọng lực (gravity). Học sinh sẽ chế tạo và thử nghiệm các mô hình dù lượn từ vật liệu nhẹ, tìm hiểu cách diện tích bề mặt vòm dù và lỗ thoát khí ảnh hưởng đến vận tốc rơi giới hạn (terminal velocity) và độ ổn định khi hạ cánh.",
        "summary": "Bài học này tập trung vào kỹ thuật hàng không vũ trụ và động lực học chất lưu: lực cản không khí (drag), lực nâng khí động học (lift) và trọng lực (gravity). Học sinh sẽ chế tạo và thử nghiệm các mô hình dù lượn từ vật liệu nhẹ, tìm hiểu cách diện tích bề mặt vòm dù và lỗ thoát khí ảnh hưởng đến vận tốc rơi giới hạn (terminal velocity) và độ ổn định khi hạ cánh.",
        "scenario": "Nhóm em là các kỹ sư hàng không vũ trụ được giao nhiệm vụ thiết kế một hệ thống dù hạ cánh khẩn cấp cho một khoang đổ bộ thám hiểm. Chiếc dù phải bung đều ngay khi thả, hãm tối đa vận tốc rơi tự do và đưa kiện hàng mẫu hạ cánh êm ái, trúng đích.",
        "criteria": [
            "Dù phải mang được tải trọng thử nghiệm (vòng đệm kim loại) từ độ cao 2 mét xuống đất với thời gian rơi chậm nhất có thể.",
            "Hạ cánh chính xác và ổn định bên trong vòng tròn mục tiêu có đường kính 1 mét trên sàn nhà."
        ],
        "constraints": [
            "Chỉ sử dụng các vật liệu nhẹ được cung cấp (túi nilon, khăn giấy, dây chỉ dù, băng dính).",
            "Thời gian thả thử nghiệm được tính trung bình qua ít nhất 3 lần thả liên tiếp."
        ]
    },
    "Kỹ thuật không lưu": {
        "theoryNotes": "Trong bài học này, học sinh sẽ tìm hiểu kỹ thuật đằng sau hệ thống kiểm soát không lưu (Air Traffic Control - ATC) hiện đại. Học sinh làm việc theo nhóm để đánh giá dữ liệu đường bay, điều phối khoảng cách an toàn giữa các máy bay theo chuẩn hàng không quốc tế, và giải quyết bài toán xung đột không gian vùng trời thông qua phần mềm mô phỏng không lưu của NASA.",
        "summary": "Trong bài học này, học sinh sẽ tìm hiểu kỹ thuật đằng sau hệ thống kiểm soát không lưu (Air Traffic Control - ATC) hiện đại. Học sinh làm việc theo nhóm để đánh giá dữ liệu đường bay, điều phối khoảng cách an toàn giữa các máy bay theo chuẩn hàng không quốc tế, và giải quyết bài toán xung đột không gian vùng trời thông qua phần mềm mô phỏng không lưu của NASA.",
        "scenario": "Nhóm em là một nhóm kỹ sư kiểm soát không lưu (Air Traffic Control - ATC) được giao nhiệm vụ vận hành và tối ưu hóa hệ thống kiểm soát không phận tại Khu vực 44 ở Hoa Kỳ (Sector 44). Sử dụng phần mềm mô phỏng không lưu của NASA, các em cần lập kế hoạch điều chỉnh lộ trình và tốc độ để 3 máy bay bay cách nhau tối thiểu 4 dặm hải lý khi tiếp cận sân bay Modesto (MOD) mà không bao giờ vi phạm khoảng cách nguy hiểm 3 hải lý.",
        "criteria": [
            "Điều phối thành công 3 chuyến bay đến điểm hạ cánh Modesto (MOD) mà không vi phạm khoảng cách an toàn tối thiểu 3 hải lý giữa các máy bay.",
            "Tối ưu hóa thời gian bay để chuyến bay cuối cùng hạ cánh sớm nhất có thể."
        ],
        "constraints": [
            "Chỉ được thay đổi vận tốc và lộ trình góc cua theo các mức cho phép trong hệ thống điều khiển.",
            "Không được để bất kỳ máy bay nào bay ra ngoài ranh giới Khu vực 44 (Sector 44)."
        ]
    },
    "Phóng tên lửa nước": {
        "theoryNotes": "Trong bài học này, học sinh sẽ tìm hiểu các nguyên lý khí động học và định luật III Newton (hành động và phản ứng) thông qua việc chế tạo và phóng tên lửa nước từ chai nhựa tái chế. Học sinh sẽ nghiên cứu tỷ lệ thể tích nước tối ưu, áp suất nén của khí, vai trò của cánh đuôi dẫn hướng và trọng tâm khí động học để tên lửa bay thẳng và đạt độ cao tối đa.",
        "summary": "Trong bài học này, học sinh sẽ tìm hiểu các nguyên lý khí động học và định luật III Newton (hành động và phản ứng) thông qua việc chế tạo và phóng tên lửa nước từ chai nhựa tái chế. Học sinh sẽ nghiên cứu tỷ lệ thể tích nước tối ưu, áp suất nén của khí, vai trò của cánh đuôi dẫn hướng và trọng tâm khí động học để tên lửa bay thẳng và đạt độ cao tối đa.",
        "scenario": "Nhóm em là các kỹ sư hàng không vũ trụ được giao thử thách thiết kế, tối ưu hóa khí động học và thử nghiệm phóng một mô hình tên lửa nước từ chai nhựa. Thử thách yêu cầu tên lửa đạt độ cao tối đa và quỹ đạo bay ổn định nhất bằng cách tính toán chính xác lượng nước nạp và hình dạng cánh đuôi.",
        "criteria": [
            "Tên lửa nước phải phóng lên theo quỹ đạo thẳng đứng, đạt độ cao tối thiểu 15 mét.",
            "Các cánh đuôi giữ nguyên vị trí, thân tên lửa chịu được áp suất nén 40-60 psi mà không bị rò rỉ."
        ],
        "constraints": [
            "Chỉ sử dụng vỏ chai nhựa PET chứa đồ uống có ga (không dùng chai nước khoáng mỏng).",
            "Tuân thủ nghiêm ngặt quy tắc an toàn bệ phóng, đứng cách xa tối thiểu 5 mét khi bơm khí."
        ]
    },
    "Tái chế giấy lớp học": {
        "theoryNotes": "Trong bài học này, học sinh sẽ tìm hiểu về kỹ thuật môi trường, chu trình tái chế sợi xenlulozo và quy trình sản xuất giấy bền vững. Học sinh sẽ tự tay nghiền bột giấy phế liệu của lớp học, lọc bỏ tạp chất, tạo màng sợi trên khung lưới, ép khử nước và sấy khô để tạo ra những tờ giấy tái chế mới có độ dai và khả năng viết tốt.",
        "summary": "Trong bài học này, học sinh sẽ tìm hiểu về kỹ thuật môi trường, chu trình tái chế sợi xenlulozo và quy trình sản xuất giấy bền vững. Học sinh sẽ tự tay nghiền bột giấy phế liệu của lớp học, lọc bỏ tạp chất, tạo màng sợi trên khung lưới, ép khử nước và sấy khô để tạo ra những tờ giấy tái chế mới có độ dai và khả năng viết tốt.",
        "scenario": "Nhóm em là các kỹ sư môi trường được giao nhiệm vụ thiết kế một quy trình tái chế giấy khép kín cho lớp học nhằm giảm thiểu lượng rác thải giấy hàng ngày. Các em sẽ thu gom giấy báo, tài liệu in hỏng, nghiền thành bột giấy và đúc khuôn để tạo ra những tấm thiệp hoặc sổ ghi chép hữu ích.",
        "criteria": [
            "Tạo ra ít nhất một tờ giấy tái chế kích thước tối thiểu 10x15 cm có độ dày đồng đều.",
            "Bề mặt giấy đủ mịn và dai để có thể viết hoặc vẽ bằng bút chì và bút dạ mà không bị rách."
        ],
        "constraints": [
            "Chỉ sử dụng giấy vụn đã qua sử dụng trong lớp học, nước ấm và khung lưới lọc thủ công.",
            "Không sử dụng hóa chất tẩy trắng công nghiệp gây độc hại."
        ]
    },
    "Tinh thể đường": {
        "theoryNotes": "Bài học này hướng dẫn học sinh tìm hiểu về hóa học vật liệu, cấu trúc mạng tinh thể và sự kết tinh từ dung dịch quá bão hòa (supersaturated solution). Học sinh sẽ tìm hiểu vai trò của diện tích bề mặt tiếp xúc, tốc độ hòa tan và ảnh hưởng của các tâm mầm kết tinh (nucleation sites) trên sợi dây đối với kích thước và hình thái của tinh thể đường phèn.",
        "summary": "Bài học này hướng dẫn học sinh tìm hiểu về hóa học vật liệu, cấu trúc mạng tinh thể và sự kết tinh từ dung dịch quá bão hòa (supersaturated solution). Học sinh sẽ tìm hiểu vai trò của diện tích bề mặt tiếp xúc, tốc độ hòa tan và ảnh hưởng của các tâm mầm kết tinh (nucleation sites) trên sợi dây đối với kích thước và hình thái của tinh thể đường phèn.",
        "scenario": "Nhóm em là các nhà khoa học vật liệu nghiên cứu quá trình nuôi cấy tinh thể. Các em sẽ hòa tan các loại đường có độ thô khác nhau trong nước sôi để tạo dung dịch bão hòa, sau đó quan sát và kiểm chứng giả thuyết về hình thái tinh thể hình thành dưới kính hiển vi.",
        "criteria": [
            "Tạo ra các tinh thể đường bám đều xung quanh sợi dây sau 7 ngày kết tinh.",
            "So sánh và ghi nhận định lượng sự khác biệt về hình thái tinh thể giữa các loại đường ban đầu (đường cát, đường bột, đường khối)."
        ],
        "constraints": [
            "Phải đun dung dịch đường dưới sự giám sát an toàn của giáo viên.",
            "Bình thủy tinh nuôi tinh thể phải được đặt ở nơi yên tĩnh, tránh rung lắc trong suốt thời gian nuôi."
        ]
    },
    "Đường cắt ngang dành cho Kỳ Nhông": {
        "theoryNotes": "Bài học STEM về thiết kế cầu vượt sinh thái và lối đi an toàn cắt ngang đường cao tốc dành cho động vật hoang dã (Kỳ nhông và các loài lưỡng cư). Học sinh tìm hiểu về bảo tồn đa dạng sinh học, tính kết nối cảnh quan sinh thái, và các giải pháp kỹ thuật hạ tầng giao thông xanh giúp động vật di cư an toàn qua đường mà không bị xe cộ va quẹt.",
        "summary": "Bài học STEM về thiết kế cầu vượt sinh thái và lối đi an toàn cắt ngang đường cao tốc dành cho động vật hoang dã (Kỳ nhông và các loài lưỡng cư). Học sinh tìm hiểu về bảo tồn đa dạng sinh học, tính kết nối cảnh quan sinh thái, và các giải pháp kỹ thuật hạ tầng giao thông xanh giúp động vật di cư an toàn qua đường mà không bị xe cộ va quẹt.",
        "scenario": "Nhóm em là các kỹ sư sinh thái và hạ tầng giao thông được giao nhiệm vụ thiết kế một tuyến đường hầm vượt sinh thái an toàn bên dưới một con đường liên tỉnh để đàn kỳ nhông có thể di chuyển từ khu rừng đến vùng đầm lầy sinh sản vào mùa xuân mà không bị xe cộ cán phải.",
        "criteria": [
            "Lối đi sinh thái phải có bề mặt giữ được độ ẩm tự nhiên để da của kỳ nhông không bị khô khi bò qua.",
            "Lối đi phải nối liền hai khu sinh cảnh và chịu được rung chấn từ mặt đường phía trên."
        ],
        "constraints": [
            "Chỉ sử dụng các vật liệu mô phỏng tự nhiên (đất ẩm, rêu, sỏi, ống nhựa, lá khô).",
            "Không được có các gờ cạnh sắc nhọn có thể làm tổn thương động vật."
        ]
    },
    "Đơn giản hóa độ phức tạp trong thuật toán": {
        "theoryNotes": "Bài học này giúp học sinh khám phá khái niệm độ phức tạp tính toán (Computational Complexity) và ký hiệu Big-O thông qua các trò chơi mô phỏng và bài toán thực tế (như bài toán Ao hoa súng và hàm tăng trưởng mũ). Học sinh sẽ so sánh sự khác nhau giữa độ phức tạp tuyến tính O(n), độ phức tạp đa thức O(n^2) và độ phức tạp hàm mũ O(2^n), từ đó hiểu tại sao các kỹ sư phần mềm phải liên tục tối ưu hóa thuật toán để hệ thống máy tính xử lý lượng dữ liệu khổng lồ trong thời gian ngắn nhất.",
        "summary": "Bài học này giúp học sinh khám phá khái niệm độ phức tạp tính toán (Computational Complexity) và ký hiệu Big-O thông qua các trò chơi mô phỏng và bài toán thực tế (như bài toán Ao hoa súng và hàm tăng trưởng mũ). Học sinh sẽ so sánh sự khác nhau giữa độ phức tạp tuyến tính O(n), độ phức tạp đa thức O(n^2) và độ phức tạp hàm mũ O(2^n), từ đó hiểu tại sao các kỹ sư phần mềm phải liên tục tối ưu hóa thuật toán để hệ thống máy tính xử lý lượng dữ liệu khổng lồ trong thời gian ngắn nhất.",
        "scenario": "Nhóm em là các kỹ sư khoa học máy tính được giao thử thách phân tích, mô phỏng và đánh giá độ phức tạp thuật toán của các bài toán tăng trưởng dữ liệu. Thông qua bài toán 'Ao hoa súng', các em sẽ chứng minh sự bùng nổ hàm mũ và đề xuất giải thuật tối ưu hóa.",
        "criteria": [
            "Xác định chính xác quy luật tăng trưởng hàm mũ O(2^n) trong bài toán ao hoa súng.",
            "Đề xuất thuật toán tìm kiếm và xử lý dữ liệu với độ phức tạp tối ưu hơn."
        ],
        "constraints": [
            "Biểu diễn các bước thuật toán bằng lưu đồ khối (flowchart) hoặc giả mã (pseudocode) chuẩn mực.",
            "Kiểm chứng kết quả bằng bảng số liệu định lượng."
        ]
    },
    "Bẻ khóa thế giới mã vạch": {
        "theoryNotes": "Bài học này hướng dẫn học sinh khám phá cấu trúc toán học và kỹ thuật quét quang học của mã vạch (UPC - Universal Product Code). Học sinh tìm hiểu cách máy quét laser đọc chuỗi vạch đen và khoảng trắng nhị phân, thuật toán kiểm tra chữ số checksum modulo 10 để phát hiện sai sót khi quét, cũng như lịch sử ra đời của công nghệ nhận dạng tự động thay đổi ngành bán lẻ toàn cầu.",
        "summary": "Bài học này hướng dẫn học sinh khám phá cấu trúc toán học và kỹ thuật quét quang học của mã vạch (UPC - Universal Product Code). Học sinh tìm hiểu cách máy quét laser đọc chuỗi vạch đen và khoảng trắng nhị phân, thuật toán kiểm tra chữ số checksum modulo 10 để phát hiện sai sót khi quét, cũng như lịch sử ra đời của công nghệ nhận dạng tự động thay đổi ngành bán lẻ toàn cầu.",
        "scenario": "Nhóm em là các kỹ sư hệ thống thông tin được giao nhiệm vụ phân tích cấu trúc mã vạch UPC trên 5 mặt hàng thực tế. Các em sẽ giải mã chuỗi nhị phân, tính toán kiểm tra chữ số kiểm tra (check digit) bằng thuật toán modulo 10 và thiết kế một mã vạch tùy biến cho sản phẩm sáng tạo của lớp.",
        "criteria": [
            "Tính toán chính xác chữ số kiểm tra modulo 10 cho chuỗi 12 chữ số mã vạch UPC.",
            "Phác thảo bản thiết kế mã vạch nhận dạng sản phẩm mới tuân thủ đúng tỷ lệ vạch và khoảng trắng."
        ],
        "constraints": [
            "Chỉ sử dụng thước kẻ, bút chì đen và bảng tra cứu cơ sở dữ liệu mã vạch UPC.",
            "Trình bày rõ ràng công thức toán học kiểm tra tính hợp lệ của mã."
        ]
    },
    "Mạch điện từ khối bột": {
        "theoryNotes": "Bài học này hướng dẫn học sinh khám phá các khái niệm cơ bản về mạch điện kín, chất dẫn điện và chất cách điện thông qua việc tự chế tạo và sử dụng khối bột nhào dẫn điện (từ bột mì, muối, nước chanh) và bột nhào cách điện (từ bột mì, đường, nước khử ion). Học sinh sẽ tìm hiểu cách dòng electron chuyển động qua các ion trong chất điện phân, phân biệt cực dương/âm của đèn LED, và thiết kế các tác phẩm điêu khắc phát sáng sinh động.",
        "summary": "Bài học này hướng dẫn học sinh khám phá các khái niệm cơ bản về mạch điện kín, chất dẫn điện và chất cách điện thông qua việc tự chế tạo và sử dụng khối bột nhào dẫn điện (từ bột mì, muối, nước chanh) và bột nhào cách điện (từ bột mì, đường, nước khử ion). Học sinh sẽ tìm hiểu cách dòng electron chuyển động qua các ion trong chất điện phân, phân biệt cực dương/âm của đèn LED, và thiết kế các tác phẩm điêu khắc phát sáng sinh động.",
        "scenario": "Nhóm em là các kỹ sư điện - vật liệu tí hon được giao nhiệm vụ tạo ra một tác phẩm điêu khắc nghệ thuật phát sáng bằng cách kết hợp bột nhào dẫn điện và bột nhào cách điện. Tác phẩm cần có ít nhất 2 đèn LED cùng phát sáng ổn định từ một khối pin 4 viên pin AA mà không bị đoản mạch.",
        "criteria": [
            "Mạch điện hoạt động tốt, thắp sáng ít nhất 2 đèn LED có màu sắc khác nhau.",
            "Sử dụng lớp bột cách điện hợp lý để ngăn ngừa dòng điện rò hoặc hiện tượng chập mạch."
        ],
        "constraints": [
            "Chỉ sử dụng bột dẫn điện, bột cách điện, hộp pin 4xAA và đèn LED siêu sáng an toàn.",
            "Không được cắm trực tiếp hai chân đèn LED vào nguồn điện mà không qua khối bột cản trở dòng."
        ]
    },
    "Thiết kế dụng cụ cắt băng keo": {
        "theoryNotes": "Bài học này hướng dẫn học sinh vận dụng thiết kế công thái học (Ergonomics) và nguyên lý cơ học (đòn bẩy, góc cắt răng cưa, ma sát) để chế tạo dụng cụ cắt băng dính cầm tay hỗ trợ người khuyết tật hoặc người chỉ có thể thao tác bằng một tay. Học sinh sẽ phân tích góc đặt lưỡi dao, lực tì giữ cuộn băng và thiết kế ngàm giữ an toàn chống cắt vào ngón tay.",
        "summary": "Bài học này hướng dẫn học sinh vận dụng thiết kế công thái học (Ergonomics) và nguyên lý cơ học (đòn bẩy, góc cắt răng cưa, ma sát) để chế tạo dụng cụ cắt băng dính cầm tay hỗ trợ người khuyết tật hoặc người chỉ có thể thao tác bằng một tay. Học sinh sẽ phân tích góc đặt lưỡi dao, lực tì giữ cuộn băng và thiết kế ngàm giữ an toàn chống cắt vào ngón tay.",
        "scenario": "Em là một nhóm kỹ sư đã được giao nhiệm vụ thiết kế một máy cắt băng keo cầm tay dành cho người có sức lực hạn chế và chỉ có thể sử dụng một tay. Dụng cụ phải giữ cuộn băng ổn định, cắt đứt dứt khoát đoạn băng theo độ dài mong muốn và đảm bảo ngón tay người dùng hoàn toàn an toàn.",
        "criteria": [
            "Cắt được đoạn băng dính có chiều dài mong muốn chỉ bằng thao tác một tay.",
            "Lưỡi cắt được che chắn an toàn, không gây nguy hiểm cho người sử dụng."
        ],
        "constraints": [
            "Chỉ sử dụng vật liệu an toàn (bìa cứng, que gỗ, kẹp ghim, dao cắt răng cưa nhựa).",
            "Trọng lượng tổng thể không vượt quá 300 gram để dễ dàng cầm nắm."
        ]
    },
    "Thiết kế thiết bị hỗ trợ": {
        "theoryNotes": "Trong bài học này, học sinh tìm hiểu về kỹ thuật trong các thiết bị hỗ trợ thích ứng (như xe lăn, khung tập đi, nẹp cố định chi thể, chi giả cơ học). Học sinh vận dụng quy trình thiết kế kỹ thuật (EDP) để chế tạo mô hình thiết bị trợ lực an toàn, tiện lợi và nhân văn giúp người giảm khả năng vận động có thể sinh hoạt độc lập.",
        "summary": "Trong bài học này, học sinh tìm hiểu về kỹ thuật trong các thiết bị hỗ trợ thích ứng (như xe lăn, khung tập đi, nẹp cố định chi thể, chi giả cơ học). Học sinh vận dụng quy trình thiết kế kỹ thuật (EDP) để chế tạo mô hình thiết bị trợ lực an toàn, tiện lợi và nhân văn giúp người giảm khả năng vận động có thể sinh hoạt độc lập."
    },
    "Paper Bridge Design Challenge": {
        "theoryNotes": "In this lesson, students investigate structural engineering principles, load distribution, and beam strength by designing bridges made solely from folded paper sheets. Students explore how geometric folding (corrugation, accordion pleats, I-beams, triangular trusses) dramatically increases the area moment of inertia and structural rigidity of thin materials.",
        "summary": "In this lesson, students investigate structural engineering principles, load distribution, and beam strength by designing bridges made solely from folded paper sheets. Students explore how geometric folding (corrugation, accordion pleats, I-beams, triangular trusses) dramatically increases the area moment of inertia and structural rigidity of thin materials.",
        "scenario": "You are a team of civil engineers challenged to design and build a bridge span using only sheets of paper that spans a 20-centimeter chasm and supports as many weights (pennies) as possible before failure.",
        "criteria": [
            "The paper bridge must span an open gap of at least 20 cm between two block supports.",
            "The bridge must support a minimum load of 20 pennies (or 50 grams) without buckling or slipping off the supports."
        ],
        "constraints": [
            "Use only two sheets of standard letter paper and no tape or glue on the bridge span.",
            "Bridges may be folded or cut, but cannot be anchored permanently to the tables."
        ]
    },
    "Take Flight!": {
        "theoryNotes": "In this aeronautical engineering lesson, students design, build, and test gliders made from simple classroom materials. Students analyze the four aerodynamic forces of flight: Lift, Weight (Gravity), Thrust, and Drag. By adjusting the wingspan, wing aspect ratio, dihedral angle, and center of gravity using paper clips, students discover how to achieve straight, stable, and long-distance flight.",
        "summary": "In this aeronautical engineering lesson, students design, build, and test gliders made from simple classroom materials. Students analyze the four aerodynamic forces of flight: Lift, Weight (Gravity), Thrust, and Drag. By adjusting the wingspan, wing aspect ratio, dihedral angle, and center of gravity using paper clips, students discover how to achieve straight, stable, and long-distance flight.",
        "scenario": "You are a team of aeronautical engineers given the challenge of creating a high-performance glider out of simple materials that can fly as straight and far as possible toward a designated target runway 15 feet away.",
        "criteria": [
            "The glider must travel a minimum distance of 15 feet (4.5 meters) in a straight flight path.",
            "The glider must remain aerodynamically stable and land intact without tumbling."
        ],
        "constraints": [
            "Use only cardstock, straws, paper clips, and tape provided in the design kit.",
            "Launches must be performed by hand from a consistent standing launch height without external catapults."
        ]
    }
}

def clean_general_text(text):
    if not isinstance(text, str):
        return text
    
    # 1. Remove PDF watermark footers
    text = re.sub(r'\s*\d*\s*Đ\s*ư\s*ợ\s*c\s*d\s*ị\s*c\s*h.*?(?:i\s*s\s*t\s*e\s*m\s*a|t\s*h\s*u\s*-\s*v\s*i\s*e\s*n|b\s*a\s*i\s*-\s*g\s*i\s*a\s*n\s*g).*?$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Đ ư ợ c dị c h bở i International STEM Association.*$', '', text)
    text = re.sub(r'B ả n g ố c:\s*h\s*t\s*t\s*p\s*s:\s*\/\s*\/.*?\/', '', text)
    text = re.sub(r'2\/1 4 W a t c h V i d e o A t:.*?(?:DOWNLOAD POWERPOINT|Materials & Preparation)', 'Materials & Preparation', text)
    
    # 2. Fix known split Vietnamese words & OCR artifacts
    replacements = [
        (r'\bthuy ền\b', 'thuyền'),
        (r'\bnguy ên\b', 'nguyên'),
        (r'\bt ốt nhất\b', 'tốt nhất'),
        (r'\bT ất cả\b', 'Tất cả'),
        (r'\btr ải nghiệm\b', 'trải nghiệm'),
        (r'\btr ời\b', 'trời'),
        (r'\bmặt tr ời\b', 'mặt trời'),
        (r'\bT r ái Đất\b', 'Trái Đất'),
        (r'\bMặt T r ời\b', 'Mặt Trời'),
        (r'\bT r ái đất\b', 'Trái Đất'),
        (r'\bT r ong\b', 'Trong'),
        (r'\bt r ong\b', 'trong'),
        (r'\bT rình\b', 'Trình'),
        (r'\bt rình\b', 'trình'),
        (r'\bT rả\b', 'Trả'),
        (r'\bt rả\b', 'trả'),
        (r'\bT riển\b', 'Triển'),
        (r'\bt riển\b', 'triển'),
        (r'\bT rước\b', 'Trước'),
        (r'\bt rước\b', 'trước'),
        (r'\bT ruy\b', 'Truy'),
        (r'\bt ruy\b', 'truy'),
        (r'\bKiểm tr a\b', 'Kiểm tra'),
        (r'\bkiểm tr a\b', 'kiểm tra'),
        (r'\bthảo luậný\b', 'thảo luận ý'),
        (r'\bbằngít\b', 'bằng ít'),
        (r'\bsúngở\b', 'súng ở'),
        (r'\bha y\b', 'hay'),
        (r'\bt oàn\b', 'toàn'),
        (r'\bt oán\b', 'toán'),
        (r'\bk eo\b', 'keo'),
        (r'\bkhung bên dưới:\s*T rình bà y\b', 'khung bên dưới: Trình bày'),
        (r'\bNhóm emi\b', 'Nhóm em'),
        (r'\bmột\b', 'một'),
        (r'\bhiện\b', 'hiện'),
        (r'\bvận\b', 'vận'),
        (r'\btha y\b', 'thay'),
        (r'\bkỹ thuật\b', 'kỹ thuật'),
        (r'\bhệ thống\b', 'hệ thống'),
        (r'\ban t oàn\b', 'an toàn'),
        (r'\bhiệu quả\b', 'hiệu quả'),
        (r'\bQhát phiếu\b', 'Phát phiếu'),
        (r'\bbài tập\b', 'bài tập'),
        (r'\bKỹ thuật không lưu\b', 'Kỹ thuật không lưu'),
        (r'\bN ASA\b', 'NASA'),
        (r'\bx em\b', 'xem'),
        (r'\bthấ y\b', 'thấy'),
        (r'\bX em\b', 'Xem'),
        (r'\bviệc\b', 'việc'),
        (r'\bđảm nhận\b', 'đảm nhận'),
        (r'\blập kế hoạch\b', 'lập kế hoạch'),
        (r'\blộ trình\b', 'lộ trình'),
        (r'\btốc độ\b', 'tốc độ'),
        (r'\bdặm\b', 'dặm'),
        (r'\bModest o\b', 'Modesto'),
        (r'\bvậy\b', 'vậy'),
        (r'\bAir T r aﬃc Contr ol - A T C\b', 'Air Traffic Control - ATC'),
        (r'\bAir T raffic\b', 'Air Traffic'),
        (r'\bSect or 44\b', 'Sector 44'),
        (r'\bcott on\b', 'cotton'),
        (r'\bNewt on\b', 'Newton'),
        (r'\bHƯ Ớ N G DẪ N T R I Ể N K H A I H O Ạ T Đ Ộ N G\b', 'HƯỚNG DẪN TRIỂN KHAI HOẠT ĐỘNG'),
        (r'\bsản yuất giấ y\b', 'sản xuất giấy'),
        (r'\bgiấ y\b', 'giấy'),
        (r'\bTình hiểu\b', 'Tìm hiểu'),
        (r'\bv ào\b', 'vào'),
        (r'\bx em x ét\b', 'xem xét'),
        (r'\by em yét\b', 'xem xét'),
        (r'\bu ồn uại\b', 'tồn tại'),
        (r'\baf fect\b', 'affect'),
        (r'\bY our\b', 'Your'),
        (r'\bV igeant\b', 'Vigeant'),
        (r'\bT eams\b', 'Teams'),
        (r'\bW ith\b', 'With'),
        (r'\bT ime\b', 'Time'),
        (r'\bT ower\b', 'Tower'),
        (r'\bW aterproof\b', 'Waterproof'),
        (r'\bW riting\b', 'Writing'),
        (r'\bV ote\b', 'Vote'),
        (r'\bV est\b', 'Vest'),
        (r'\bT all\b', 'Tall'),
        (r'\bT ake\b', 'Take')
    ]
    
    for pat, rep in replacements:
        text = re.sub(pat, rep, text)
        
    # Replace any known title fix inside prose
    for bad_t, good_t in TITLE_MAP.items():
        if bad_t in text:
            text = text.replace(bad_t, good_t)
            
    return text.strip()

def clean_lecture_object(lec):
    title = lec.get("title", "")
    # Update title
    if title in TITLE_MAP:
        lec["title"] = TITLE_MAP[title]
        title = lec["title"]
        
    # If this lecture has curated replacements
    if title in CURATED_LESSONS:
        cur = CURATED_LESSONS[title]
        if "theoryNotes" in cur:
            lec["theoryNotes"] = cur["theoryNotes"]
        if "lessonPlan" in lec:
            lp = lec["lessonPlan"]
            if "overview" in lp and "summary" in cur:
                lp["overview"]["summary"] = cur["summary"]
            if "challenge" in lp:
                ch = lp["challenge"]
                if "scenario" in cur:
                    ch["scenario"] = cur["scenario"]
                if "criteria" in cur:
                    ch["criteria"] = cur["criteria"]
                if "constraints" in cur:
                    ch["constraints"] = cur["constraints"]
                    
    # Clean all strings in lecture
    def deep_clean(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, str):
                    obj[k] = clean_general_text(v)
                else:
                    deep_clean(v)
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                if isinstance(item, str):
                    obj[idx] = clean_general_text(item)
                else:
                    deep_clean(item)
    deep_clean(lec)

# Process entire dataset
for lvl in data:
    for lang in lvl.get("languages", []):
        for t in lang.get("topics", []):
            for lec in t.get("lectures", []):
                clean_lecture_object(lec)

# Save to data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Mirror to data.js
with open("data.js", "w", encoding="utf-8") as f:
    f.write("// STEM LMS Global Curriculum Dataset\n")
    f.write("window.APP_DATA = ")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Successfully cleaned all orthography, spelling, watermarks and titles across data.json and data.js!")
